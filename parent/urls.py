from django.urls import path
from parent.views import  GetStudentLastEventsView, GetStudentStatisticsView, ParentCreateView, ParentDeleteView, ParentDetailView, ParentListView, ParentLoginView

urlpatterns = [
    path('list/', ParentListView.as_view(), name='parent-list'),
	path('create/', ParentCreateView.as_view(), name='parent-create'),
	path('update/', ParentCreateView.as_view(), name='parent-update'),
    path('parentDetail/<int:pk>/', ParentDetailView.as_view(), name='parent-detail'),
    path('<int:pk>/delete/', ParentDeleteView.as_view(), name='parent-delete'),
    path('parent-student-stats/<int:id>/', GetStudentStatisticsView.as_view(), name='student-stats'),
    path('parent-student-last-events/<int:id>/', GetStudentLastEventsView.as_view(), name='student-stats'),
	path('login/', ParentLoginView.as_view(), name='student-stats'),


]
