from django.conf.urls import url
from django.urls import path
from CrudApp import views

app_name = "CrudApp"

urlpatterns = [
    path('',views.index,name='index'),
    path('add_musician/',views.musician,name='musician_form'),
    path('add_album/',views.album_form,name='album_form'),
    path('album_list/<int:artist_id>/',views.album_list,name='album_list'),
    path('edit_artist/<int:artist_id>/',views.edit_artist,name='edit_artist'),
    path('edit_album/<int:album_id>/', views.edit_album, name='edit_album'),


]
