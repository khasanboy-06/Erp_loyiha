from django.shortcuts import render, get_object_or_404, redirect
from users.permissions import StudentRequiredMixin
from django.views import View
from users.models import Student, Team
from .forms import HomeworkForm
from .models import Lesson, Homework

class StudentDashboardView(StudentRequiredMixin, View):
    def get(self, request):
        return render(request, 'students/dashboard.html')

class StudentGroupView(StudentRequiredMixin, View):
    def get(self, request):
        student = Student.objects.get(user=request.user)
        return render(request, 'students/guruhlarim.html', context={"student":student})
    

class StudentLessonsView(StudentRequiredMixin, View):
    def get(self, request, group_id):
        team = get_object_or_404(Team, id=group_id)
        lessons = team.lessons.all()
        return render(request, 'students/lessons.html', context={"lessons":lessons})
    

class HomeworkView(StudentRequiredMixin, View):
    def get(self, request, lesson_id):
        form = HomeworkForm()
        return render(request, 'students/homework.html', context={"form":form})
    
    def post(self, request, lesson_id):
        lesson = get_object_or_404(Lesson, id=lesson_id)
        student = get_object_or_404(Student, user=request.user)

        form = HomeworkForm(request.POST, request.FILES)
        if form.is_valid():
            homework = Homework()
            homework.lesson = lesson
            homework.student = student
            homework.description = form.cleaned_data['description']
            homework.homework_file = form.cleaned_data['homework_file']

            homework.save()

            lesson.homework_status = True
            lesson.save()

            return redirect('/')