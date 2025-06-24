import datetime
from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from reviews.models import Activity, CheckIn, ReviewModel
from student.models import Student
from student.serializers import StudentSerializer
from django.db.models import Avg
from calendar import month_abbr
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.http import JsonResponse
from collections import Counter
from django.db.models import Avg, Count



from student.utils import BEHAVIOR_MAP, EMOTION_MAP, SKILL_MAP
from teacher.models import Teacher

# Create your views here.
class StudentDetailView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentReviewSummaryView(generics.GenericAPIView):
    def get(self, request, student_id):
        student = get_object_or_404(Student, id=student_id)

        reviews = ReviewModel.objects.filter(student_id=student_id)

        fields = [
            'interation',
            'concentration',
            'autonomy',
            'comunication',
            'problemSolving',
            'compreension',
        ]

        result = {field: [] for field in fields}

        current_month = datetime.datetime.now().month

        for month in range(1, current_month + 1):
            monthly_reviews = reviews.filter(date__month=month)

            if monthly_reviews.exists():
                aggregated = monthly_reviews.aggregate(
                    **{f"{field}_avg": Avg(field) for field in fields}
                )

                for field in fields:
                    result[field].append({
                        "value": round(aggregated.get(f"{field}_avg") or 0, 2),
                        "label": month_abbr[month]
                    })
            else:
                for field in fields:
                    result[field].append({
                        "value": 0,
                        "label": month_abbr[month]
                    })

        data = {
            'student': {
                'id': student.id,
                'name': student.name,
                'class': student.school_class.name if student.school_class else '',
                'year': student.school_class.year if student.school_class else '',
                'currentYear': timezone.now().year
            },
            'reviews': result
        }

        return Response(data)



def annual_report(request, student_id):
    current_year = timezone.now().year

    # Checkins (como já fizemos antes)
    checkins_qs = CheckIn.objects.filter(student_id=student_id, date__year=current_year)
    total_checkins = checkins_qs.count()
    checkins_counts = (
        checkins_qs
        .values('emoction_id')
        .annotate(count=Count('emoction_id'))
    )
    checkins_dict = {c['emoction_id']: c['count'] for c in checkins_counts}
    emotion_data = []
    for emo_id, emo_info in EMOTION_MAP.items():
        count = checkins_dict.get(emo_id, 0)
        percent = (count / total_checkins * 100) if total_checkins > 0 else 0
        emotion_data.append({
            "id": str(emo_id),
            "title": emo_info["title"],
            "image": emo_info["image"],
            "percent": round(percent, 2)
        })

    # Reviews
    reviews_qs = ReviewModel.objects.filter(student_id=student_id, date__year=current_year)

    skill_avgs = reviews_qs.aggregate(**{f"{m['field']}_avg": Avg(m['field']) for m in SKILL_MAP})
    behavior_avgs = reviews_qs.aggregate(**{f"{m['field']}_avg": Avg(m['field']) for m in BEHAVIOR_MAP})

    # SKILLS
    skill_list = []
    for m in SKILL_MAP:
        avg = skill_avgs.get(f"{m['field']}_avg") or 0
        skill_list.append({
            "id": m["id"],
            "title": m["title"],
            "image": m["image"],
            "avg": avg
        })
    total_skill_avg = sum(item["avg"] for item in skill_list)
    skill_data = []
    for item in skill_list:
        percent = (item["avg"] / total_skill_avg * 100) if total_skill_avg > 0 else 0
        skill_data.append({
            "id": item["id"],
            "title": item["title"],
            "image": item["image"],
            "percent": round(percent, 2)
        })

    # BEHAVIORS
    behavior_list = []
    for m in BEHAVIOR_MAP:
        avg = behavior_avgs.get(f"{m['field']}_avg") or 0
        behavior_list.append({
            "id": m["id"],
            "title": m["title"],
            "image": m["image"],
            "avg": avg
        })
    total_behavior_avg = sum(item["avg"] for item in behavior_list)
    behavior_data = []
    for item in behavior_list:
        percent = (item["avg"] / total_behavior_avg * 100) if total_behavior_avg > 0 else 0
        behavior_data.append({
            "id": item["id"],
            "title": item["title"],
            "image": item["image"],
            "percent": round(percent, 2)
        })

    # ORDENAÇÃO
    emotion_data.sort(key=lambda x: x['percent'], reverse=True)
    skill_data.sort(key=lambda x: x['percent'], reverse=True)
    behavior_data.sort(key=lambda x: x['percent'], reverse=True)

    student = get_object_or_404(Student, id=student_id)

    return JsonResponse({
        'student': {
            'id': student.id,
            'name': student.name,
            "class": student.school_class.name,
            "year": student.school_class.year,
            "currentYear": current_year
        },
        "emotions": emotion_data,
        "skills": skill_data,
        "behaviors": behavior_data
    })




class StudentActivitiesSummaryView(generics.GenericAPIView):
    def get(self, request, student_id):
        current_year = timezone.now().year

        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found.'}, status=status.HTTP_404_NOT_FOUND)

        activities = Activity.objects.filter(student_id=student_id, date__year=current_year)

        total_activities = activities.count()
        if total_activities == 0:
            return Response({
                'student': {
                    'id': student.id,
                    'name': student.name,
                    "class": student.school_class.name if student.school_class else '',
                    "year": student.school_class.year if student.school_class else '',
                    "currentYear": current_year
                },
                'participationChart': [],
                'typeActivityChart': []
            })

        # Contabiliza participações
        participation_counts = Counter(activities.values_list('participation', flat=True))

        PARTICIPATION_LABELS = {
            '1': 'Não participou',
            '2': 'Parcialmente',
            '3': 'Participou',
        }

        PARTICIPATION_COLORS = {
            '1': '#4CAF50',
            '2': '#2196F3',
            '3': '#FF9800',
        }

        participation_chart = [
            {
                "value": round((participation_counts.get(key, 0) / total_activities) * 100, 2),
                "label": PARTICIPATION_LABELS[key],
                "color": PARTICIPATION_COLORS[key],
                "text": f"{round((participation_counts.get(key, 0) / total_activities) * 100, 2)}%"
            }
            for key in PARTICIPATION_LABELS.keys()
        ]

        # Contabiliza tipos de atividade
        type_counts = Counter(activities.values_list('activity_type', flat=True))

        ACTIVITY_COLORS = {
            '1': '#4CAF50',   # Linguagem
            '2': '#2196F3',   # Cognitivo
            '3': '#FF9800',   # Motricidade
            '4': '#9C27B0',   # Sensorial
            '5': '#FFC107',   # Autonomia
            '6': '#F44336',   # Participação
        }

        ACTIVITY_LABELS = {
            '1': 'Linguagem',
            '2': 'Cognitivo',
            '3': 'Motricidade',
            '4': 'Sensorial',
            '5': 'Autonomia',
            '6': 'Participação',
        }

        type_activity_chart = [
            {
                'value': round((type_counts.get(key, 0) / total_activities) * 100, 2),
                'label': ACTIVITY_LABELS[key],
                'frontColor': ACTIVITY_COLORS[key],
                'text': f"{round((type_counts.get(key, 0) / total_activities) * 100, 2)}%"
            }
            for key in ACTIVITY_LABELS.keys()
        ]

        data = {
            'student': {
                'id': student.id,
                'name': student.name,
                "class": student.school_class.name if student.school_class else '',
                "year": student.school_class.year if student.school_class else '',
                "currentYear": current_year
            },
            'pieData': participation_chart,
            'typeActivityChart': type_activity_chart
        }

        return Response(data, status=status.HTTP_200_OK)

class TeacherStudentsOptionsView(generics.GenericAPIView):
    queryset=Student.objects.all(   )
    def get(self, request, teacher_id):
        try:
            teacher = Teacher.objects.get(id=teacher_id)
        except Teacher.DoesNotExist:
            return Response({"detail": "Teacher not found."}, status=status.HTTP_404_NOT_FOUND)

        if not teacher.school_class:
            return Response([], status=status.HTTP_200_OK)

        students = Student.objects.filter(school_class=teacher.school_class)

        data = [
            {"label": student.name, "value": student.id}
            for student in students
        ]

        return Response(data, status=status.HTTP_200_OK)
