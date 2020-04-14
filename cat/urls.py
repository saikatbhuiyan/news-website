from django.urls import path

from . import views


urlpatterns = [
  path('panel/news/cat_list/', views.cat_list, name='cat_list'),
  path('panel/news/cat_add/', views.cat_add, name='cat_add'),
  path('panel/news/cat_delete/<int:pk>', views.cat_delete, name='cat_delete'),
]