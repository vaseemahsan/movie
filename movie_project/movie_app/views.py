from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import movieform
from .models import movies

# Create your views here.
def index(request):
    movie=movies.objects.all()
    context={
        "movie_list":movie
    }
    return render(request,'index.html',context)

def details(request,movie_id):
    movie=movies.objects.get(id=movie_id)
    return render(request,'details.html', {'movie': movie})

def add_movie(request):
    if request.method == "POST":
        name=request.POST.get('name')
        description=request.POST.get('description')
        year=request.POST.get('year')
        image=request.FILES['image']
        movie=movies(name=name,description=description,year=year,image=image)
        movie.save()

    return render(request,'add.html')


def update(request, id):
    movie=movies.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})

def delete(request,id):
    if request.method =="POST":
        movie=movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')

