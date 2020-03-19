from django.db import models

# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    hit_song = models.CharField(max_length=100)
    def __str__(self):
        return self.title


# albums = [
#     Album('An Innocent Man', 'Billy Joel',
#           'doo-wop, soft-rock, soul', 'Uptown Girl'),
#     Album('Songs in the Key of Life', 'Stevie Wonder',
#           'soul, funk, R&B, jazz fusion', 'Sir Duke'),
#     Album('Unplugged', 'Eric Clapton', 'blues, acoustic rock', 'Layla')
# ]