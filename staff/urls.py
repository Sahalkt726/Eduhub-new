from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('staff_dashboard/', staff_dashboard, name='staff_dashboard'),
    path('manage-courses/', manage_courses, name='manage_courses'),
    path('delete-course/<int:course_id>/', delete_course, name='delete_course'), 
    path('update-course/<int:course_id>/', update_course, name='update_course'),
    path('notifications/', create_notification, name='notifications'),
    path('edit_staff_details/<int:user_id>/', edit_staff_details, name='edit_staff_details'),
    path('feedback', staff_feedback , name='staff_feedback'),
    path('add_question/', add_question, name='add_question'),
    path('delete/question/<int:question_id>/', delete_question, name='delete_question'),
    path('question_list', question_list, name='question_list'),
    path('upload/', upload_study_material, name='upload_study_material'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
