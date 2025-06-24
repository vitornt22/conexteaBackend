from django.urls import path
from .views import (
    CheckInCreateView,
    ActionModelCreateView,
    ActivityCreateView,
    ReviewModelCreateView,
    EducationPlanModelCreateView,
    get_education_plan_by_student,
    
)

urlpatterns = [
    path('checkin/create/', CheckInCreateView.as_view(), name='checkin-create'),
    path('action/create/', ActionModelCreateView.as_view(), name='action-create'),
    path('activity/create/', ActivityCreateView.as_view(), name='activity-create'),
    path('review/create/', ReviewModelCreateView.as_view(), name='review-create'),
    path('educationplan/create/', EducationPlanModelCreateView.as_view(), name='educationplan-create'),
	path('get-student-pei/<int:student_id>/', get_education_plan_by_student, name='educationplan-create'),
]
