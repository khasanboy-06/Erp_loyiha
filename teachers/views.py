from django.shortcuts import render, get_object_or_404
from django.views import View
from users.permissions import TeacherRequiredMixin
from users.models import Teacher, Team
from django.contrib.auth.mixins import LoginRequiredMixin


class TeacherDashboardView(TeacherRequiredMixin, View):
    def get(self, request):
        return render(request, 'teachers/teacher_dashboard.html')
    


class TeacherTeamsView(TeacherDashboardView, View):
    def get(self, request):
        teacher = get_object_or_404(Teacher, user = request.user)
        teams = teacher.teams.all()
        return render(request, 'teachers/guruhlarim.html', context={"teams":teams})
    

class LessonView(View):
    def get(self, request, group_id):
        team = get_object_or_404(Team, id=group_id)
        lessons = team.lessons.all()
        return render(request, 'teachers/lessons.html', context={"lessons":lessons})
    

class TeamStudentsView(TeacherRequiredMixin, View):
    def get(self, request):
        teacher = get_object_or_404(Teacher, user=request.user)
        students = teacher.students.all()
        return render(request, 'teachers/students.html', context={"students":students})
    
