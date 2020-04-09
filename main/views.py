from django.shortcuts import render, get_object_or_404, redirect

from .models import Main


def home(request):
  site = Main.objects.get(pk=1)

  # sitename = "MySite | Home"
  return render(request, 'front/home.html', {'site': site})
  
def about(request):
  # sitename = "MySite | About"
  site = Main.objects.get(pk=1)

  return render(request, 'front/about.html', {'site': site})
