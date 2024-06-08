from django.shortcuts import render
from django.views import View
from users.permissions import TeacherRequiredMixin


class TeacherDashboardView(TeacherRequiredMixin, View):
    def get(self, request):
        return render(request, 'teachers/teacher_dashboard.html')