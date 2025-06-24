import datetime
from rest_framework import generics
from django.utils import timezone
from student.models import Student
from django.shortcuts import HttpResponse
from django.http import JsonResponse
from django.utils import timezone


from .models import CheckIn, ActionModel, Activity, ReviewModel, EducationPlanModel
from .serializers import (
    CheckInSerializer, 
    ActionModelSerializer, 
    ActivitySerializer, 
    ReviewModelSerializer, 
    EducationPlanModelSerializer
)

class CheckInCreateView(generics.CreateAPIView):
    queryset = CheckIn.objects.all()
    serializer_class = CheckInSerializer

class ActionModelCreateView(generics.CreateAPIView):
    queryset = ActionModel.objects.all()
    serializer_class = ActionModelSerializer

class ActivityCreateView(generics.CreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class ReviewModelCreateView(generics.CreateAPIView):
    queryset = ReviewModel.objects.all()
    serializer_class = ReviewModelSerializer

class EducationPlanModelCreateView(generics.CreateAPIView):
    queryset = EducationPlanModel.objects.all()
    serializer_class = EducationPlanModelSerializer


def get_education_plan_by_student(request, student_id):
    try:
        # Pega o primeiro PEI do es tudante
        pei = EducationPlanModel.objects.filter(student_id=student_id).first()

        if pei is None:
            return JsonResponse({'error': 'Nenhum PEI encontrado para este estudante.'}, status=404)

        student = pei.student

        student_data = {
            'id': student.id,
            'name': student.name,
            'class': student.school_class.name if student.school_class else '',
            'year': student.school_class.year if student.school_class else '',
            'currentYear': datetime.datetime.now().year
        }

        pei_data = {
            'id': pei.id,
            'year': pei.year,
            'start_date': pei.start_date,
            'end_date': pei.end_date,
            'objectives': pei.objectives,
            'resource': pei.resource,
            'report1': pei.report1,
            'report2': pei.report2,
            'student': student_data
        }

        return JsonResponse(pei_data)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
