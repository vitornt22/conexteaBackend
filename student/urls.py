from django.urls import path
from student.views import StudentActivitiesSummaryView, StudentReviewSummaryView, TeacherStudentsOptionsView, annual_report

urlpatterns = [    
	path('<int:student_id>/review-summary/', StudentReviewSummaryView.as_view(), name='student-review-summary'),
	path('annual-report/<int:student_id>/', annual_report, name='annual_report'),
	path('activities-summary/<int:student_id>', StudentActivitiesSummaryView.as_view(), name='student-activities-summary'),
	path('teacher-students-options/<int:teacher_id>/', TeacherStudentsOptionsView.as_view(), name='teacher-students-options')



]