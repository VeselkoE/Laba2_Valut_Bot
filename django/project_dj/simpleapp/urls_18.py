from django.contrib import admin
from django.urls import path
from . import views
from .views import PostList18, PostDetail18

urlpatterns = [
    path('', views.start_page_18, name='task18'),
    #path('news/', views.news_list, name='news_list'),
    path('news/', PostList18.as_view(), name='news_list'),
    path('news/<int:pk>/', PostDetail18.as_view(), name='news_details_18'),
    #path('news/<int:news_id>/', views.news_details, name='news_details_18'),
]
