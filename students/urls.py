from django.urls import path
from .views import StudentDashboardView, StudentGroupView, StudentLessonsView, HomeworkView

app_name = 'students'


urlpatterns = [
    path('dashboard/', StudentDashboardView.as_view(), name='dashboard'),
    path('guruhlarim/', StudentGroupView.as_view(), name='guruhlarim'),
    path('lessons/<int:group_id>/', StudentLessonsView.as_view(), name='lessons'),
    path('homework/<int:lesson_id>/', HomeworkView.as_view(), name='homework'),
]