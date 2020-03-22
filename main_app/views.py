from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album, Genre
from .forms import AddTrackForm

# CBVs


class AlbumCreate(CreateView):
    model = Album
    fields = ['title', 'artist']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist']


class AlbumDelete(DeleteView):
    model = Album
    success_url = '/albums/'


# Create your views here.


def home(request):
    return HttpResponse('<h1>Hello World</h1>')


def about(request):
    return render(request, 'about.html')


def albums_index(request):
    albums = Album.objects.all()
    return render(request, 'albums/index.html', {'albums': albums})


def albums_detail(request, album_id):
    album = Album.objects.get(id=album_id)
    if album.track_set != None:
        tracks = album.track_set.all().order_by('track_num')
    else:
        tracks = []
    genres_not_listed = Genre.objects.exclude(
        id__in=album.genres.all().values_list('id'))
    add_track_form = AddTrackForm()
    return render(request, 'albums/detail.html', {
        'album': album,
        'tracks': tracks,
        'genres': genres_not_listed,
        'add_track_form': add_track_form
    })


def add_track(request, album_id):
    form = AddTrackForm(request.POST)
    if form.is_valid():
        new_track = form.save(commit=False)
        new_track.album_id = album_id
        new_track.save()
    return redirect('detail', album_id=album_id)


def assoc_genre(request, album_id, genre_id):
    Album.objects.get(id=album_id).genres.add(genre_id)
    return redirect('detail', album_id=album_id)
