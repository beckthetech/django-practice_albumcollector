from django.shortcuts import render
from django.http import HttpResponse


class Album:  # Note that parens are optional if not inheriting from another class
    def __init__(self, title, artist, genre, hit_song):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.hit_song = hit_song


albums = [
    Album('An Innocent Man', 'Billy Joel',
          'doo-wop, soft-rock, soul', 'Uptown Girl'),
    Album('Songs in the Key of Life', 'Stevie Wonder',
          'soul, funk, R&B, jazz fusion', 'Sir Duke'),
    Album('Unplugged', 'Eric Clapton', 'blues, acoustic rock', 'Layla')
]

# Create your views here.


def home(request):
    return HttpResponse('<h1>Hello World</h1>')


def about(request):
    return render(request, 'about.html')


def albums_index(request):
    return render(request, 'albums/index.html', {'albums': albums})
