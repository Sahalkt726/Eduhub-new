from django.urls import path
from . views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('student_dashboard/', student_dashboard, name='student_dashboard'),
    path('student_enroll_course/', student_course, name='student_course'),
    path('enrolled-course-videos/<int:course_id>/', enrolled_course_videos, name='enrolled_course_videos'),
    path('enroll/<int:course_id>/', enroll_course, name='enroll_course'),
    path('delete_enrolled_course/<int:enrollment_id>/', delete_enrolled_course, name='delete_enrolled_course'),
    path('student_notifications/', student_notifications, name='student_notification'),
    path('notifications/delete/<int:notification_id>/', delete_notification, name='delete_notification'),    
    path('edit_student_details/<int:user_id>/', edit_student_details, name='edit_student_details'),
    path('feedback/<int:staff_id>/', student_feedback, name='student_feedback'),
    path('questions/', display_questions, name='display_questions'),
    path('evaluate/', evaluate_answers, name='evaluate_answers'),
    path('view-study-materials/', view_study_materials, name='view_study_materials'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)