from django.urls import path
from .views import TeacherDashboardView, TeacherTeamsView, TeacherGroupView, TeacherStudentsView, Profile, TeacherCreateLessonView, EditProfileView

app_name = 'teachers'

urlpatterns = [
    path('teacher/', TeacherDashboardView.as_view(), name='teacher'),
    path('guruhlarim/', TeacherTeamsView.as_view(), name='guruhlarim'),
    path('lessons/<int:team_id>/', TeacherGroupView.as_view(), name='lessons'),
    path('students/<int:team_id>/', TeacherStudentsView.as_view(), name='students'),
    path('profile/', Profile.as_view(), name='profile'),
    path('create-lesson/<int:team_id>/', TeacherCreateLessonView.as_view(), name='create_lesson'),
    path('edit-profile/<int:id>/', EditProfileView.as_view(), name='edit_profile'),
]