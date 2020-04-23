import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import FileSystemStorage

from main.models import Main
from .models import News
from subcat.models import SubCat
from cat.models import Category


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

    cat = SubCat.objects.all()

    if request.method == 'POST':

          newstitle = request.POST.get('newstitle')
          newscat = request.POST.get('newscat')
          newstxtshort = request.POST.get('newstxtshort')
          newstxt = request.POST.get('newstxt')

          if newstitle == "" or newstxtshort == "" or newstxt == "" or newscat == "":
            error = "All Fields Requirded"
            return render(request, 'back/error.html', {'error': error})

          try:
              myfile = request.FILES['myfile']
              fs = FileSystemStorage()
              filename = fs.save(myfile.name, myfile)
              url = fs.url(filename)

              if str(myfile.content_type).startswith("image"):

                  if myfile.size < 500000 :
                      catname = SubCat.objects.get(pk=newscat).name
                      ocatid = SubCat.objects.get(pk=newscat).catid

                      b = News(name=newstitle, short_txt=newstxtshort, body_txt=newstxt, picname=filename, picurl=url, catname=catname, date=today,
                               time=time, writer=request.user, catid=newscat, ocatid=ocatid, show=0)
                      b.save()

                      count = len(News.objects.filter(ocatid=ocatid))
                      b = Category.objects.get(pk=ocatid)
                      b.count = count
                      b.save()

                      return redirect('news_list')

                  else:
                      error = "File Size Is More Than 5 MB!"
                      return render(request, 'back/error.html', {'error': error})

              else:
                  fs.delete(filename)
                  error = "File Type Is Not Supported"
                  return render(request, 'back/error.html', {'error': error})

          except:
              error = "Please upload a image!"
              return render(request, 'back/error.html', {'error': error})

    return render(request, 'back/news_add.html', {'cat': cat})


def news_delete(request, pk):

    try:
        news = News.objects.get(pk=pk)
        fs = FileSystemStorage()
        fs.delete(news.picname)
        ocatid = News.objects.get(pk=pk).ocatid

        news.delete()

        count = len(News.objects.filter(ocatid=ocatid))
        b = Category.objects.get(pk=ocatid)
        b.count = count
        b.save()

    except:
        error = "Something Wrong!"
        return render(request, 'back/error.html', {'error': error})

    return redirect('news_list')


def news_edit(request, pk):
    if len(News.objects.filter(pk=pk)) == 0:
        error = "No News Found"
        return render(request, 'back/error.html', {'error': error})

    news = News.objects.get(pk=pk)
    cat = SubCat.objects.all()
    name = SubCat.objects.get(pk=news.catid).catname

    if request.method == 'POST':

          newstitle = request.POST.get('newstitle')
          newscat = request.POST.get('newscat')
          newstxtshort = request.POST.get('newstxtshort')
          newstxt = request.POST.get('newstxt')

          if newstitle == "" or newstxtshort == "" or newstxt == "" or newscat == "":
                error = "All Fields Requirded"
                return render(request, 'back/error.html', {'error': error})

          try:
              myfile = request.FILES['myfile']
              fs = FileSystemStorage()
              filename = fs.save(myfile.name, myfile)
              url = fs.url(filename)

              if str(myfile.content_type).startswith("image"):

                  if myfile.size < 500000 :
                      catname = SubCat.objects.get(pk=newscat).name

                      b = News.objects.get(pk=pk)

                      fss = FileSystemStorage()
                      fss.delete(news.picname)

                      b.name = newstitle
                      b.short_txt = newstxtshort
                      b.body_txt = newstxt
                      b.writer = b.writer
                      b.picname = filename
                      b.picurl = url
                      b.catid = newscat
                      b.catname = catname
                      b.save()
                      return redirect('news_list')

                  else:
                      error = "File Size Is More Than 5 MB!"
                      return render(request, 'back/error.html', {'error': error})

              else:
                  fs.delete(filename)
                  error = "File Type Is Not Supported"
                  return render(request, 'back/error.html', {'error': error})

          except:
              catname = SubCat.objects.get(pk=newscat).name

              b = News.objects.get(pk=pk)

              b.name = newstitle
              b.short_txt = newstxtshort
              b.body_txt = newstxt
              b.writer = b.writer
              b.catid = newscat
              b.catname = catname
              b.save()
              return redirect('news_list')

    context = {
        'pk': pk,
        'news': news,
        'cat': cat,
        'name': name,
    }
    return render(request, 'back/news_edit.html', context)

