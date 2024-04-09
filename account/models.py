from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
  

class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True) 
    profile_image = models.ImageField(upload_to='staff_profile_images/', blank=True, null=True)
   

    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        self.user.delete()
        super().delete(*args, **kwargs)
       

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, null=True)    
    profile_image = models.ImageField(upload_to='student_profile_images/', blank=True, null=True)

    def __str__(self):
        return self.name
    
    def delete(self, *args, **kwargs):
        self.user.delete()
        super().delete(*args, **kwargs)
    


