from django.urls import path
from .views import StudentDashboardView, StudentGroupView, StudentLessonsView, HomeworkView, HomeDetailView, Profile

app_name = 'students'


urlpatterns = [
    path('dashboard/', StudentDashboardView.as_view(), name='dashboard'),
    path('guruhlarim/', StudentGroupView.as_view(), name='guruhlarim'),
    path('lessons/<int:group_id>/', StudentLessonsView.as_view(), name='lessons'),
    path('homework/<int:lesson_id>/', HomeworkView.as_view(), name='homework'),
    path('homework-detail/<int:lesson_id>/', HomeDetailView.as_view(), name='homework_detail'),
    path('profile/', Profile.as_view(), name='profile'), 

]