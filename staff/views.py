from django.shortcuts import render,redirect,get_object_or_404
from account . models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.urls import reverse
from django.http import HttpResponseNotFound
from . models import *
from student . models import *
from django.contrib import messages






@login_required
def staff_dashboard(request):
    total_students = Student.objects.count()
    staff_profile = Staff.objects.get(user=request.user)
    profile_image = staff_profile.profile_image.url if staff_profile.profile_image else None
    return render(request, 'staff_templates/staff_dashboard.html', {'profile_image': profile_image,'total_students': total_students})


def manage_courses(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.staff = request.user.staff  
            course.save()
            return redirect('manage_courses')
    else:
        form = CourseForm()
    courses = Course.objects.filter(staff=request.user.staff)
    return render(request, 'staff_templates/manage_course.html', {'form': form, 'courses': courses})


def delete_course(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
        if request.method == 'POST':
            course.delete()
            return redirect('manage_courses')
    except Course.DoesNotExist:
        return HttpResponseNotFound("Course not found")
    return redirect(reverse('manage_courses'))


def update_course(request, course_id):
    try:
        course = Course.objects.get(pk=course_id)
        if request.method == 'POST':
            form = CourseForm(request.POST, request.FILES, instance=course)
            if form.is_valid():
                form.save()
                return redirect('manage_courses')
        else:
            form = CourseForm(instance=course)
        return render(request, 'staff_templates/update_course.html', {'form': form})
    except Course.DoesNotExist:
        return HttpResponseNotFound("Course not found")



def create_notification(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            students = Student.objects.all() 
            for student in students:
                Notification.objects.create(user=student.user, message=message)
            messages.success(request, "Your message has been sent successfully.")
            return redirect('notifications')  
    else:
        form = NotificationForm()
    return render(request, 'staff_templates/notifications.html', {'form': form})



def edit_staff_details(request,user_id):
    user = request.user
    if request.method == 'POST':
        form = StaffChangeForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            staff = Staff.objects.get(user=user)
            staff.name = user.username
            staff.email = user.email
            staff.profile_image = user.profile_image
            staff.save()
            return redirect('staff_dashboard')  
    else:
        form = StaffChangeForm(instance=user)
    return render(request, 'staff_templates/edit_staff_details.html', {'form': form})


def staff_feedback(request):
    staff_member = request.user.staff
    feedbacks = Feedback.objects.filter(staff_member=staff_member)
    return render(request, 'staff_templates/staff_feedback.html', {'feedbacks': feedbacks})


def question_list(request):
    questions = Question.objects.all()
    choices = Choice.objects.all() 
    return render(request, 'staff_templates/question_list.html', {'questions': questions,'choices':choices})




def delete_question(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return redirect('question_list')

def add_question(request):
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        choice_formset = ChoiceFormSet(request.POST)
        if question_form.is_valid() and choice_formset.is_valid():
            question = question_form.save()
            for form in choice_formset:
                choice = form.save(commit=False)
                choice.question = question
                choice.save()
            return redirect('add_question')  
    else:
        question_form = QuestionForm()
        choice_formset = ChoiceFormSet()
    return render(request, 'staff_templates/add_question.html', {'question_form': question_form, 'choice_formset': choice_formset})


def upload_study_material(request):
    if request.method == 'POST':
        form = StudyMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            study_material = form.save(commit=False)
            study_material.uploaded_by = request.user
            study_material.save()
            return redirect('upload_study_material')
    else:
        form = StudyMaterialForm()
    
    return render(request, 'staff_templates/upload_study_material.html', {'form': form})
