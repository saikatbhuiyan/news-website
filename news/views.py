from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect

from main.models import Main
from .models import News


def news_detail(request, word):

  news = News.objects.filter(name=word)
  site = Main.objects.get(pk=1)

  return render(request, 'front/news_detail.html', {'news': news, 'site': site})
  