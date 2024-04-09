from django.db import models
from account . models import *
# Create your models here.

class Course(models.Model):
    staff=models.ForeignKey(Staff,on_delete = models.CASCADE)
    course_image=models.ImageField(upload_to='Course_images/')
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=250)
    

    def __str__(self):
        return self.title
    



    
class Contact(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    message=models.TextField(max_length=250)

    def __str__(self):
        return self.name
    
    
