from django.db import models
from account . models import *
from home . models import *

# Create your models here

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.title}"
    

class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=200)
    video_url = models.URLField()

    def __str__(self):
        return self.title



class Feedback(models.Model):
    staff_member = models.ForeignKey(Staff, on_delete=models.CASCADE)
    message = models.TextField() 

    def __str__(self):
        return self.message
    


