from django.contrib import admin
from . models import *
from . forms import *

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Staff)
admin.site.register(Student)

