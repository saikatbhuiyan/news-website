from django.shortcuts import render, get_object_or_404, redirect

from .models import Main


def home(request):
  sitename = "MySite | Home"
  return render(request, 'front/home.html', {'sitename': sitename})
  
def about(request):
  sitename = "MySite | About"

  return render(request, 'front/about.html', {'sitename': sitename})
