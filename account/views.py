from django.shortcuts import render, redirect
from . forms import *
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages




def staff_signup(request):
    if request.method == 'POST':
        form = StaffSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.save()
            staff = Staff.objects.create(
                user=user,
                name=user.username,
                email=user.email,
                profile_image=form.cleaned_data['profile_image']
            )
            return redirect('login')
    else:
        form = StaffSignupForm()
    return render(request, 'staff_templates/staff_signup.html', {'form': form})


def student_signup(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_student = True
            user.save()
            staff = Student.objects.create(
                user=user,
                name=user.username,
                email=user.email, 
                profile_image=form.cleaned_data['profile_image']
            )
            return redirect('login')
    else:
        form = StudentSignupForm()
    return render(request, 'student_templates/student_signup.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect('staff_dashboard')
                elif user.is_student:
                    return redirect('student_dashboard')
                else:
                    pass
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = LoginForm()
    return render(request, 'home_templates/login.html', {'form': form})


def change_password(request):
    user = request.user
    if request.method == 'POST':
        password_form = PasswordChangeForm(user, request.POST)
        if password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user) 
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
    else:
        password_form = PasswordChangeForm(user)
    return render(request, 'home_templates/change_password.html', {'password_form': password_form})
    


def user_logout(request):
    logout(request)
    return redirect('home')