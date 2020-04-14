from django.urls import path

from . import views


urlpatterns = [
  path('panel/news/subcat_list/', views.subcat_list, name='subcat_list'),
  path('panel/news/subcat_add/', views.subcat_add, name='subcat_add'),
  # path('panel/news/cat_delete/<int:pk>', views.cat_delete, name='cat_delete'),
]