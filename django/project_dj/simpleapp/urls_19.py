#from django.contrib import admin
from django.urls import path
from . import views
from .views import PostList19, PostDetail19

urlpatterns = [
    path('', views.start_page_19, name='task19'),
    path('news/', PostList19.as_view(), name='news_list_by_page'),
    path('news/<int:news_id>/', PostDetail19.as_view(), name='news_details_19'),
    # path('news/', views.new_list_by_pages, name='new_list_by_pages'),
    # path('news/<int:news_id>/', views.news_details_19, name='news_details_19'),
]
