from django.shortcuts import render, get_object_or_404, redirect

from .models import Main
from news.models import News
from cat.models import Category

def home(request):
  site = Main.objects.get(pk=1)
  news = News.objects.all().order_by('-pk')
  cat = Category.objects.all()
  # sitename = "MySite | Home"
  return render(request, 'front/home.html', {'site': site, 'news': news, 'cat': cat})
  
def about(request):
  # sitename = "MySite | About"
  site = Main.objects.get(pk=1)

  return render(request, 'front/about.html', {'site': site})


def panel(request):

  return render(request, 'back/home.html')