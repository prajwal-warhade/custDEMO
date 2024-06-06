from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Home, name='home'),
    path('about', About, name='about'),
    path('contact', Contact, name='contact'),
    path('gallery', Gallery, name='gallery'),
]