from django.urls import path

from . import views


urlpatterns = [
  path('panel/news/subcat_list/', views.subcat_list, name='subcat_list'),
  path('panel/news/subcat_add/', views.subcat_add, name='subcat_add'),
  path('panel/news/subcat_delete/<int:pk>', views.subcat_delete, name='subcat_delete'),
]