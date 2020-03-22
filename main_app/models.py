from django.db import models
from django.urls import reverse
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

RELEASES = (
    ('O', 'original release'),
    ('R', 're-release'),
    ('C', 'cover'),
)

class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    hit_song = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'album_id': self.id})


class Track(models.Model):
    track_num = models.IntegerField('Track Number',
                                    validators=[MinValueValidator(
                                        1), MaxValueValidator(20)]
                                    )
    name = models.CharField(max_length=100)
    release = models.CharField(
        max_length=1,
        choices=RELEASES,
        default=RELEASES[0][0]
    )
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Track: {self.track_num}, {self.name} is a{'n' if self.release == RELEASES[0][0] else ''} {self.get_release_display()}"