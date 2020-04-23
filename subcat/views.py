from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import datetime
from django.shortcuts import render, get_object_or_404, redirect

from .models import SubCat
from cat.models import Category

@login_required(login_url='/login/')
def subcat_list(request):
    subcat = SubCat.objects.all()

    return render(request, 'back/subcat_list.html', {'subcat': subcat})

@login_required(login_url='/login/')
def subcat_add(request):

    cat = Category.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        catid = request.POST.get('cat')
        name = name.capitalize()

        if name == "":
            error = "All Field is required!"
            return render(request, 'back/error.html', {'error': error})

        if len(SubCat.objects.filter(name=name)) != 0:
            error = "This name already used!"
            return render(request, 'back/error.html', {'error': error})

        catname = Category.objects.get(pk=catid).name
        subcat = SubCat(name=name, catname=catname, catid=catid)
        subcat.save()
        return redirect('subcat_list')

    return render(request, 'back/subcat_add.html', {'cat': cat})

@login_required(login_url='/login/')
def subcat_delete(request, pk):
    try:
        subcat = SubCat.objects.get(pk=pk)
        subcat.delete()

    except:
        error = "Something Wrong!"
        return render(request, 'back/error.html', {'error': error})

    return redirect('subcat_list')