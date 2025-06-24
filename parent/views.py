import datetime
import random
from rest_framework import generics
from itertools import chain
from rest_framework_simplejwt.tokens import RefreshToken
from parent.utils import ACTIVITY_TYPE_MAP, EMOTION_MAP, EMOTION_PORTUGUESE_MAP, PARTICIPATION_MAP, PICTOGRAM_MAP, SUBJECT_MAP_PT
from utils.choices import  RELATIONSHIP_DEGREE_CHOICES
from .models import Parent
from .serializers import LoginSerializer, ParentSerializer
from rest_framework.response import Response
from rest_framework import status
from student.models import Student
from reviews.models import CheckIn, ReviewModel, Activity
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from school.models import User
from parent.models import Parent
from utils.choices import EDUCATION_LEVEL_CHOICES, RELATIONSHIP_DEGREE_CHOICES, SEX_CHOICES
import random



class ParentListView(generics.ListAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    
class ParentUpdateView(generics.UpdateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class ParentCreateView(generics.CreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    
class ParentDeleteView(generics.DestroyAPIView):
    queryset = Parent.objects.all()

class ParentDetailView(generics.RetrieveAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer



class GetStudentStatisticsView(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        student_id = kwargs.get('id')

        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        current_year = datetime.datetime.now().year

        # Filtrar registros do ano atual
        total_checkins = CheckIn.objects.filter(
            student_id=student_id,
            date__year=current_year
        ).count()

        total_activities = Activity.objects.filter(
            student_id=student_id,
            date__year=current_year
        ).count()

        total_assessments = ReviewModel.objects.filter(
            student_id=student_id,
            date__year=current_year
        ).count()

        # Emoções - filtrar checkins do ano atual com emoções válidas
        emotion_counts = {name: 0 for name in EMOTION_MAP.values()}

        checkins = CheckIn.objects.filter(
            student_id=student_id,
            emoction_id__in=EMOTION_MAP.keys(),
            date__year=current_year
        )

        emotion_data = (
            checkins
            .values('emoction_id')
            .annotate(count=Count('id'))
        )

        for item in emotion_data:
            emotion_name = EMOTION_MAP.get(item['emoction_id'])
            if emotion_name:
                emotion_counts[emotion_name] = item['count']

        # Calcular percentuais
        emotion_percentages = {}
        for name, count in emotion_counts.items():
            percent = (count / total_checkins * 100) if total_checkins > 0 else 0
            emotion_percentages[name] = round(percent, 2)

        relationship = dict(RELATIONSHIP_DEGREE_CHOICES)

        label = relationship.get(student.parent.relationship_degree)  # 'Pai'


        # Montar resposta
        data = {
            "student_name": student.name,
            "relationship_degree":label, 
            "preposition": "do" if student.gender =='M' else 'da',
            "current_year": current_year,
            "school_student_class": student.school_class.name if student.school_class else "N/A",
            "total_checkins": total_checkins,
            "total_activities": total_activities,
            "total_assessments": total_assessments,
            "emotions": emotion_percentages
        }

        return Response(data, status=status.HTTP_200_OK)

class GetStudentLastEventsView(generics.GenericAPIView):
    queryset = Student.objects.none()  # Evita erro do DRF

    def get(self, request, *args, **kwargs):
        student_id = kwargs.get('id')

        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)

        # Buscar dados relacionados
        checkins = student.checkins.select_related('teacher').all()
        actions = student.actions.select_related('teacher').all()
        activities = student.activities.select_related('teacher').all()
        reviews = student.reviews.select_related('teacher').all()

        # Montar listas formatadas

        checkin_data = [
            {
                "Type": "CheckIn",
                "studentName": student.name, 
                "subjectName": SUBJECT_MAP_PT.get(c.teacher.subject, "N/A") if c.teacher and hasattr(c.teacher, 'subject') else "N/A",
                "TeacherName": f"Prof. {c.teacher.name}" if c.teacher else "N/A",
                "date": c.date.strftime('%Y-%m-%d'),
                "othersInformations": {
                    "id": c.id,
                    "emoctionSelected": c.emoction_id,
                    "emoctionName": EMOTION_PORTUGUESE_MAP.get(c.emoction_id, "Desconhecido"),
                    "emoctionPath": EMOTION_MAP.get(c.emoction_id, "").lower(),
                    "teacherDescription": c.description,
                    "teacherId": c.teacher.id if c.teacher else None
                }
            }
            for c in checkins
        ]

        action_data = [
            {
                "Type": "Action",
                "studentName": student.name, 
                "subjectName": SUBJECT_MAP_PT.get(a.teacher.subject, "N/A") if a.teacher and hasattr(a.teacher, 'subject') else "N/A",
                "TeacherName": f"Prof. {a.teacher.name}" if a.teacher else "N/A",
                "date": a.date.strftime('%Y-%m-%d'),
                "othersInformations": {
                    "id": a.id,
                    "imageSelected": a.emoction_id,
                    "imageName": PICTOGRAM_MAP.get(a.emoction_id, {}).get("name", "Desconhecido"),
                    "imagePath": PICTOGRAM_MAP.get(a.emoction_id, {}).get("path", ""),
                    "teacherDescription": a.description,
                    "teacherId": a.teacher.id if a.teacher else None
                }
            }
            for a in actions
        ]

        activity_data = [
            {
                "Type": "Activitie",
                "studentName": student.name, 
                "subjectName": SUBJECT_MAP_PT.get(act.teacher.subject, "N/A") if act.teacher and hasattr(act.teacher, 'subject') else "N/A",
                "TeacherName": f"Prof. {act.teacher.name}" if act.teacher else "N/A",
                "date": act.date.strftime('%Y-%m-%d'),
                "othersInformations": {
                    "id": act.id,
                    "activityType": act.activity_type,
                    "typeName": ACTIVITY_TYPE_MAP.get(act.activity_type, "Desconhecido"),
                    "description": act.description,
                    "participationSelect": act.participation,
                    "participationSelectedLabel": PARTICIPATION_MAP.get(act.participation, "Desconhecido"),
                    "performance": act.student_performance
                }
            }
            for act in activities
        ]

        review_data = [
            {
                "Type": "Review",
                "studentName": student.name, 
                "subjectName": SUBJECT_MAP_PT.get(r.teacher.subject, "N/A") if r.teacher and hasattr(r.teacher, 'subject') else "N/A",
                "TeacherName": f"Prof. {r.teacher.name}" if r.teacher else "N/A",
                "date": r.date.strftime('%Y-%m-%d'),
                "othersInformations": {
                    "id": r.id,
                    "habilities": {
                        "interation": r.interation,
                        "concentration": r.concentration,
                        "autonomy": r.autonomy,
                        "comunication": r.comunication,
                        "problemSolving": r.problemSolving,
                        "compreension": r.compreension
                    },
                    "behavior": {
                        "regulation": r.regulation,
                        "respect": r.respect,
                        "resistance": r.resistance,
                        "challenges": r.challenges,
                        "participation": r.participation,
                        "punctuality": r.punctuality
                    }
                }
            }
            for r in reviews
        ]

        # Combinar todos os dados numa lista só
        combined = list(chain(checkin_data, action_data, activity_data, review_data))

        # Ordenar por data desc (mais recente primeiro)
        combined_sorted = sorted(
            combined,
            key=lambda x: datetime.datetime.strptime(x["date"], "%Y-%m-%d"),
            reverse=True
        )

        # Pegar os 100 mais recentes
        combined_sorted = combined_sorted[:100]

        return Response(combined_sorted, status=status.HTTP_200_OK)
    

class ParentLoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            parent = Parent.objects.get(username=username)
        except Parent.DoesNotExist:
            return Response({'detail': 'Usuário não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        if parent.password != password:
            return Response({'detail': 'Senha inválida.'}, status=status.HTTP_401_UNAUTHORIZED)

        # Agora usamos o User associado para gerar o token
        refresh = RefreshToken.for_user(parent.user)
        tokens = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        # Pega o student relacionado
        student = getattr(parent, 'student', None)
        student_id = student.id if student else None

        return Response({
            'tokens': tokens,
            'name': parent.name,
            'email': parent.email,
            'user_type': 'parent',
            'student_id': student_id
        }, status=status.HTTP_200_OK)


