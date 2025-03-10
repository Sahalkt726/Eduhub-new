from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',index,name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('courses/', courses, name='courses'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


