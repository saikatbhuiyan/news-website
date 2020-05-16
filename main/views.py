from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.core.files.storage import FileSystemStorage

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
  popnews = News.objects.all().order_by('-show')
  popnews2 = News.objects.all().order_by('-show')[:3]


  context = {
    'site': site,
    'news': news,
    'cat': cat,
    'subcat': subcat,
    'lastnews': lastnews,
    'popnews': popnews,
    'popnews2': popnews2,
  }

  # sitename = "MySite | Home"
  return render(request, 'front/home.html', context)
  
def about(request):
  # sitename = "MySite | About"
  site = Main.objects.get(pk=1)
  news = News.objects.all().order_by('-pk')
  cat = Category.objects.all()
  subcat = SubCat.objects.all()
  lastnews = News.objects.all().order_by('-pk')[:3]
  popnews2 = News.objects.all().order_by('-show')[:3]


  context = {
    'site': site,
    'news': news,
    'cat': cat,
    'subcat': subcat,
    'lastnews': lastnews,
    'popnews2': popnews2,
  }

  return render(request, 'front/about.html',  context)

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


@login_required(login_url='/login/')
def site_setting(request):
  perm = 0
  # for i in request.user.groups.all():
  #   if i.name == "masteruser": perm = 1
  #
  # if perm == 0:
  #   error = "Access Denied"
  #   return render(request, 'back/error.html', {'error': error})

  if request.method == 'POST':

    name = request.POST.get('name')
    tell = request.POST.get('tell')
    fb = request.POST.get('fb')
    tw = request.POST.get('tw')
    yt = request.POST.get('yt')
    link = request.POST.get('link')
    txt = request.POST.get('txt')

    if fb == "": fb = "#"
    if tw == "": tw = "#"
    if yt == "": yt = "#"
    if link == "": link = "#"

    if name == "" or tell == "" or txt == "":
      error = "All Fields Requirded"
      return render(request, 'back/error.html', {'error': error})

    try:

      myfile = request.FILES['myfile']
      fs = FileSystemStorage()
      filename = fs.save(myfile.name, myfile)
      url = fs.url(filename)

      picurl = url
      picname = filename

    except:

      picurl = "-"
      picname = "-"

    try:

      myfile2 = request.FILES['myfile2']
      fs2 = FileSystemStorage()
      filename2 = fs2.save(myfile2.name, myfile2)
      url2 = fs2.url(filename2)

      picurl2 = url2
      picname2 = filename2

    except:

      picurl2 = "-"
      picname2 = "-"

    b = Main.objects.get(pk=1)
    b.name = name
    b.tell = tell
    b.fb = fb
    b.tw = tw
    b.yt = yt
    b.link = link
    b.about = txt

    if picurl != "-": b.picurl = picurl
    if picname != "-": b.picname = picname
    if picurl2 != "-":  b.picurl2 = picurl2
    if picname2 != "-": b.picname2 = picname2

    b.save()

  site = Main.objects.get(pk=1)

  return render(request, 'back/setting.html', {'site': site})

@login_required(login_url='/login/')
def about_setting(request):

  if request.method == 'POST':

    txt = request.POST.get('txt')

    if txt == "" :
      error = "All Fields Requirded"
      return render(request, 'back/error.html', {'error': error})

    b = Main.objects.get(pk=1)
    b.abouttxt = txt
    b.save()

  about = Main.objects.get(pk=1).abouttxt

  return render(request, 'back/about_setting.html', {'about': about})


def contact(request):

  site = Main.objects.get(pk=1)
  news = News.objects.all().order_by('-pk')
  cat = Category.objects.all()
  subcat = SubCat.objects.all()
  lastnews = News.objects.all().order_by('-pk')[:3]
  popnews2 = News.objects.all().order_by('-show')[:3]


  context = {
    'site': site,
    'news': news,
    'cat': cat,
    'subcat': subcat,
    'lastnews': lastnews,
    'popnews2': popnews2,
  }

  return render(request, 'front/contact.html', context)

