from django.shortcuts import render, get_object_or_404, redirect

from .models import Main
from news.models import News

def home(request):
  site = Main.objects.get(pk=1)
  news = News.objects.all()
  # sitename = "MySite | Home"
  return render(request, 'front/home.html', {'site': site, 'news': news})
  
def about(request):
  # sitename = "MySite | About"
  site = Main.objects.get(pk=1)

  return render(request, 'front/about.html', {'site': site})


def panel(request):

  return render(request, 'back/home.html')