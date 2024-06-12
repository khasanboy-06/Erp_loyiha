from django.urls import path
from .views import TeacherDashboardView, TeacherTeamsView, LessonView, TeamStudentsView

app_name = 'teachers'

urlpatterns = [
    path('teacher/', TeacherDashboardView.as_view(), name='teacher'),
    path('guruhlarim/', TeacherTeamsView.as_view(), name='guruhlarim'),
    path('lessons/<int:group_id>/', LessonView.as_view(), name='lessons'),
    path('students/', TeamStudentsView.as_view(), name='students'),
]