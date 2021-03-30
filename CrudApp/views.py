from django.shortcuts import render
from django.http import HttpResponse
from CrudApp.models import Musician,Album
from CrudApp import forms
# Create your views here.

def index(request):
    musician_list = Musician.objects.order_by('first_name')

    diction = {'title':"Home Page",'musician_list':musician_list}
    return render(request,'CrudApp/index.html',context=diction)

def album_list(request,artist_id):
    artist_info = Musician.objects.get(pk=artist_id)
    album_info = Album.objects.filter(artist=artist_id)

    diction = {'title':"Album",'artist_info':artist_info,'album_info':album_info}
    return render(request,'CrudApp/album_list.html',context=diction)


def musician(request):
    form = forms.MusicianForm()
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)


    diction = {'title':"musician",'musician_form':form}
    return render(request,'CrudApp/musician_form.html',context=diction)

def album_form(request):
    form = forms.AlbumForm()

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
    diction = {'title':"album_form",'album_form':form}

    return render(request,'CrudApp/album_form.html',context=diction)
