from django.urls import path, re_path

from . import views


urlpatterns = [
  path('news/<str:word>/', views.news_detail, name='news_detail'),
  path('panel/news/list/', views.news_list, name='news_list'),
  path('panel/news/add/', views.news_add, name='news_add'),

]