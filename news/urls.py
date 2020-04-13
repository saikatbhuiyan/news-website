from django.urls import path, re_path

from . import views


urlpatterns = [
  path('news/<str:word>/', views.news_detail, name='news_detail'),
 
]