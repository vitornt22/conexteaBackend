import datetime
from django.shortcuts import get_object_or_404
from rest_framework import generics
from django.http import JsonResponse


from parent.models import Parent
from reviews.models import Activity, CheckIn, ReviewModel
from student.models import Student
from student.serializers import StudentSerializer
from .models import Teacher
from rest_framework.decorators import api_view

from .serializers import TeacherSerializer
from rest_framework.response import Response
from rest_framework import status


class TeacherListView(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    
class TeacherUpdateView(generics.UpdateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherCreateView(generics.CreateAPIView):
    queryset = Teacher.objects.all()    
    serializer_class = TeacherSerializer
    
class TeacherDeleteView(generics.DestroyAPIView):
    queryset = Teacher.objects.all()

class TeacherDetailView(generics.RetrieveAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def get(self, request, *args, **kwargs):
        teacher = self.get_object()
        teacher_data = self.get_serializer(teacher).data

        school_class = teacher.school_class

        if school_class:
            students = Student.objects.filter(school_class=school_class)

            checkin_count = CheckIn.objects.filter(student__in=students).count()
            activity_count = Activity.objects.filter(student__in=students).count()
            review_count = ReviewModel.objects.filter(student__in=students).count()
        else:
            checkin_count = 0
            activity_count = 0
            review_count = 0

        return Response({
            "teacher": teacher_data,
            "related_data": {
                "checkin_count": checkin_count,
                "activity_count": activity_count,
                "review_count": review_count
            }
        })



class GetTeacherInitialView(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        teacher_id = kwargs.get('id')

        try:
            teacher = Teacher.objects.get(id=teacher_id)
        except Teacher.DoesNotExist:
            return Response({'error': 'Teacher not found'}, status=status.HTTP_404_NOT_FOUND)

        current_year = datetime.datetime.now().year

        total_checkins = CheckIn.objects.filter(
            student__school_class=teacher.school_class,
            date__year=current_year
        ).count()

        total_activities = Activity.objects.filter(
            student__school_class=teacher.school_class,
            date__year=current_year
        ).count()

        total_students = Student.objects.filter(
            school_class=teacher.school_class
        ).count()

        students_qs = Student.objects.filter(
            school_class=teacher.school_class
        )

        students = [
                {
                'id': student.id, # It's good practice to include the ID
                'school': student.school.name if student.school else None,
                'parent': student.parent.name if student.parent else None,
                'name': student.name,
                'education_level': student.education_level,
                'gender': student.gender,
                'autism_level': student.autism_level,
                'preferences': student.preferences,
                'comorbidades': student.comorbidades, # Note: TextField with default=list might store as string
                'triggers_sensitivities': student.triggers_sensitivities,
                'birthdate': student.birthdate.isoformat() if student.birthdate else None, # Format date for JSON
                'school_class': student.school_class.name if student.school_class else None,
                'support_level': student.support_level,
                'what_helps_to_calm_down': student.what_helps_to_calm_down,
            }
            for student in students_qs
        ]

        data = {
            'teacher': {
                'id': teacher.id,
                'name': teacher.name
            },
            'currentYear': current_year,
            'totalCheckins': total_checkins,
            'totalActivities': total_activities,
            'totalStudents': total_students,
            'students': students
        }

        return Response(data, status=status.HTTP_200_OK)


@api_view(['GET'])
def students_by_teacher(request, teacher_id):
    # Buscar o professor
    teacher = get_object_or_404(Teacher, id=teacher_id)

    # Verifica se o professor tem turma
    if not teacher.school_class:
        return JsonResponse({"error": "Este professor não possui turma vinculada."}, status=400)

    # Busca os alunos da turma
    students_qs = Student.objects.filter(school_class=teacher.school_class)

    # Serializa os dados
    serializer = StudentSerializer(students_qs, many=True)

    return JsonResponse({"students": serializer.data}, safe=False)


