from django.shortcuts import render
from users.permissions import StudentRequiredMixin
from django.views import View
from users.models import Student

class StudentDashboardView(StudentRequiredMixin, View):
    def get(self, request):
        return render(request, 'students/dashboard.html')

class StudentGroupView(StudentRequiredMixin, View):
    def get(self, request):
        student = Student.objects.get(user=request.user)
        return render(request, 'students/guruhlarim.html', context={"student":student})