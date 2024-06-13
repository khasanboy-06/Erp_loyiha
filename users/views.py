from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import LoginForm, RegisterForm, ProfileForm, StudentEditForm, ResetPasswordForm
from .models import User, Student, Team, Teacher
from django.contrib.auth.mixins import LoginRequiredMixin
from .permissions import AdminRequiredMixin
from django.db.models import Q


class AdminDashboardView(AdminRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/admin_dashboard.html')

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.user_role == 'student':
                    return redirect('students/dashboard')
                elif user.user_role == 'teacher':
                    return redirect('teachers/teacher')
                elif user.user_role == 'admin':
                    return redirect('/admin-dashboard')

        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})
    

class RegisterView(AdminRequiredMixin, View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            if user.user_role == 'student':
                new_student = Student()
                new_student.user = user
                new_student.save()

            elif user.user_role == 'teacher':
                new_teacher = Teacher()
                new_teacher.user = user
                new_teacher.save()

            return redirect('/data')

        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})
    

class Data(View):
    def get(self, request):
        form = User.objects.all()
        return render(request, 'users/data.html', context={"form":form})

class Profile(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'users/profile.html')

def delete(request, id):
    data = get_object_or_404(User, id=id)
    data.delete()
    return redirect("/data")


class EditProfileView(LoginRequiredMixin, View):
    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        form = ProfileForm(instance=user)
        return render(request, 'users/edit_profile.html', {'form': form})

    def post(self, request, id):
        user = get_object_or_404(User, id=id)
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/profile') 
        return render(request, 'users/edit_profile.html', {'form': form})
    

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')
    
class GroupView(View):
    def get(self, request):
        teams = Team.objects.all()
        return render(request, 'users/groups.html', context={"teams":teams})

class StudentListView(AdminRequiredMixin, View):
    def get(self, request):
        if request.GET != {}:
            students = Student.objects.filter(Q(user__username__icontains = request.GET['search']))
        else:
            students = Student.objects.all()
        return render(request, 'users/students.html', context={'students': students})
    

class StudentByTeamView(AdminRequiredMixin, View):
    def get(self, request, id):
        team = get_object_or_404(Team, id=id)
        student = team.students.all()
        return render(request, 'users/students.html', context={"student":student})


class EditStudentView(AdminRequiredMixin, View):
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        form = StudentEditForm(instance=student)
        return render(request, 'users/edit_student.html', context={"form":form})
    
    def post(self, request, id):
        student = get_object_or_404(Student, id=id)
        form = StudentEditForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('users:students')
        form = StudentEditForm(instance=student)
        return render(request, 'users/edit_student.html', context={"form":form})

class DeleteStudentView(AdminRequiredMixin, View):
    def get(self, request, id):
        student = get_object_or_404(Student, id=id)
        user = User.objects.get(username = student.user.username)
        student.delete()
        user.delete()
        return redirect('users:students')
    
class ResetPasswordView(LoginRequiredMixin,View):
    def get(self, request):
        form = ResetPasswordForm
        return render(request, 'users/reset_password.html', {'form':form})

    def post(self, request):
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            user = request.user
            user.set_password(new_password)
            user.save()
            return redirect('/')
        form = ResetPasswordForm
        return render(request, 'users/reset_password.html', {'form':form})
