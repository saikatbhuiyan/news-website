import datetime
from django.shortcuts import render, get_object_or_404, redirect
from main.models import Main
from .models import News


def news_detail(request, word):

  news = News.objects.filter(name=word)
  site = Main.objects.get(pk=1)

  return render(request, 'front/news_detail.html', {'news': news, 'site': site})

def news_list(request):
  news = News.objects.all()

  return render(request, 'back/news_list.html', {'news': news})

def news_add(request):
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day

    if len(str(day)) == 1:
        day = "0" + str(day)
    if len(str(month)) == 1:
        month = "0" + str(month)

    today = str(year) + "/" + str(month) + "/" + str(day)
    time = str(now.hour) + ":" + str(now.minute)


    if request.method == 'POST':

          newstitle = request.POST.get('newstitle')
          # newscat = request.POST.get('newscat')
          newstxtshort = request.POST.get('newstxtshort')
          newstxt = request.POST.get('newstxt')

          if newstitle == "" or newstxtshort == "" or newstxt == "" : #or newscat == ""
            error = "All Fields Requirded"
            return render(request, 'back/error.html', {'error': error})

          b = News(name=newstitle, short_txt=newstxtshort, body_txt=newstxt, catname='Sport', date=today,
                   writer=request.user, catid=0, show=0)
          b.save()
          return redirect('news_list')

    return render(request, 'back/news_add.html')