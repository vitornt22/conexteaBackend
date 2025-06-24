from django.urls import path

from parent.views import GetStudentStatisticsView
from teacher.views import  GetTeacherInitialView, TeacherCreateView, TeacherDeleteView, TeacherDetailView, TeacherListView, students_by_teacher

urlpatterns = [
    path('list/', TeacherListView.as_view(), name='teacher-list'),
	path('create/', TeacherCreateView.as_view(), name='teacher-create'),
	path('update/', TeacherCreateView.as_view(), name='teacher-update'),
    path('<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),
    path('<int:pk>/delete/', TeacherDeleteView.as_view(), name='teacher-delete'),
	path('initial-information/<int:id>/', GetTeacherInitialView.as_view(), name='teacher-initial-informations'),
    path('students-by-teacher/<int:teacher_id>/', students_by_teacher, name='students-by-teacher'),


]
