from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from .views import home, register, comingsoon

urlpatterns = [
    path('',home, name='home'),
    # path('register/',register, name='register'),
    path('comingsoon/',comingsoon, name='comingsoon')
]
