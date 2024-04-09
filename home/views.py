from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'home_templates/index.html')

def courses(request):
    courses = Course.objects.all()
    return render(request,'home_templates/courses.html',{'courses': courses})


def about(request):
    return render(request,'home_templates/about.html')

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact=Contact(name=name,phone=phone,email=email,message=message)
        contact.save()
        messages.info(request, "Your message has been sent successfully.")        
        return redirect('/')
    else:
        return render(request,'home_templates/contact.html')
