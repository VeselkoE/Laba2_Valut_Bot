from django.contrib import admin
from django.urls import path, include
from . import views
from .views import start

urlpatterns = [
    path('', views.start, name='start'),
]