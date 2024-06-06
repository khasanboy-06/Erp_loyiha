from django.urls import path
from .views import LoginView, RegisterView, Profile, EditProfileView, LogoutView, GroupView, StudentListView, EditStudentView, DeleteStudentView, StudentByTeamView, ResetPasswordView
from .views import Data, delete

app_name = 'users'


urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('data/', Data.as_view(), name='data'),
    path('profile/', Profile.as_view(), name='profile'),
    path('delete/<int:id>/', delete, name='delete'),
    path('edit-profile/<int:id>/', EditProfileView.as_view(), name='edit_profile'),
    path('teams/', GroupView.as_view(), name='groups'),
    path('students/', StudentListView.as_view(), name='students'),
    path('edit-student/<int:id>/', EditStudentView.as_view(), name='edit_student'),
    path('delete-student/<int:id>/', DeleteStudentView.as_view(), name='delete_student'),
    path('student-by-team/<int:id>/', StudentByTeamView.as_view(), name='student_by_team'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),
]