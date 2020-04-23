from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth

from .models import Main
from news.models import News
from cat.models import Category
from subcat.models import SubCat

def home(request):
  site = Main.objects.get(pk=1)
  news = News.objects.all().order_by('-pk')
  cat = Category.objects.all()
  subcat = SubCat.objects.all()
  lastnews = News.objects.all().order_by('-pk')[:3]


  # sitename = "MySite | Home"
  return render(request, 'front/home.html', {'site': site, 'news': news, 'cat': cat, 'subcat': subcat, 'lastnews': lastnews })
  
def about(request):
  # sitename = "MySite | About"
  site = Main.objects.get(pk=1)

  return render(request, 'front/about.html', {'site': site})

@login_required(login_url='/login/')
def panel(request):

  return render(request, 'back/home.html')


def login(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)

    if user is not None:
      auth.login(request, user)
      messages.success(request, 'You are now logged in')
      return redirect('panel')

    else:
      messages.error(request, 'Invalid user')
      return redirect('login')
  else:
    return render(request, 'front/login.html')


def logout(request):
  if request.method == 'POST':
    auth.logout(request)
    messages.success(request, 'You are now logout')
  return redirect('login')