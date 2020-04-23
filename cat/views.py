from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import datetime
from django.shortcuts import render, get_object_or_404, redirect

from .models import Category

@login_required(login_url='/login/')
def cat_list(request):

  cat = Category.objects.all()

  return render(request, 'back/cat_list.html', {'cat': cat})

@login_required(login_url='/login/')
def cat_add(request):
  if request.method == 'POST':
      name = request.POST.get('name')
      name = name.capitalize()
      
      if name == "":
          error = "All Field is required!"
          return render(request, 'back/error.html', {'error': error})

      if len(Category.objects.filter(name=name)) != 0:
          error = "This name already used!"
          return render(request, 'back/error.html', {'error': error})

      cat = Category(name=name, count=0)
      cat.save()
      return redirect('cat_list')

  return render(request, 'back/cat_add.html')

@login_required(login_url='/login/')
def cat_delete(request, pk):
  try:
    cat = Category.objects.get(pk=pk)
    cat.delete()

  except:
    error = "Something Wrong!"
    return render(request, 'back/error.html', {'error': error})

  return redirect('cat_list')