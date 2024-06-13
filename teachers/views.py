from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from users.permissions import TeacherRequiredMixin
from users.models import Teacher, Team, User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateLessonForm
from students.models import Lesson, Homework
from django.urls import reverse
from users.forms import ProfileForm



class TeacherDashboardView(TeacherRequiredMixin, View):
    def get(self, request):
        return render(request, 'teachers/teacher_dashboard.html')
    

class Profile(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'teachers/profile.html')

class TeacherTeamsView(TeacherDashboardView, View):
    def get(self, request):
        teacher = get_object_or_404(Teacher, user = request.user)
        teams = teacher.teams.all()
        return render(request, 'teachers/guruhlarim.html', context={"teams":teams})
    

class TeacherGroupView(TeacherRequiredMixin, View):
    def get(self, request, team_id):
        team = get_object_or_404(Team, id=team_id)
        lessons = team.lessons.all()
        return render(request, 'teachers/lessons.html', context={'team':team, 'lessons':lessons})

    
class TeacherStudentsView(TeacherRequiredMixin, View):
    def get(self, request, team_id):
        team = get_object_or_404(Team, id=team_id)
        students = team.students.all()
        return render(request, 'teachers/students.html', context={'team':team, 'students':students})
    

class TeacherCreateLessonView(TeacherRequiredMixin, View):
    def get(self, request, team_id):
        form = CreateLessonForm()
        return render(request, 'teachers/create_lesson.html', context={"form":form})
    
    def post(self, request, team_id):
        team = get_object_or_404(Team, id=team_id)
        form = CreateLessonForm(request.POST)
        if form.is_valid():
            lesson = Lesson()
            lesson.team = team
            lesson.title = form.cleaned_data['title']
            lesson.save()
            url = reverse('teachers:lessons', args=[team_id])
            return redirect(url)
        

class EditProfileView(LoginRequiredMixin, View):
    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        form = ProfileForm(instance=user)
        return render(request, 'teachers/edit_profile.html', {'form': form})

    def post(self, request, id):
        user = get_object_or_404(User, id=id)
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/profile') 
        return render(request, 'teachers/edit_profile.html', {'form': form}) 


class TeacherStudentsLessonsView(TeacherRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')  
        lesson = get_object_or_404(Lesson, id=id)
        homeworks = Homework.objects.filter(lesson=lesson)
        students = [homework.student for homework in homeworks]
        return render(request, 'teachers/lesson_students.html', {'students': students})