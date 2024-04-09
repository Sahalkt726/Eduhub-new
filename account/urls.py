from django.urls import path
from .views import *

urlpatterns = [
    path('student_signup/', student_signup, name='student_signup'),
    path('staff_signup/', staff_signup, name='staff_signup'),
    path('change_password/', change_password, name='change_password'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
