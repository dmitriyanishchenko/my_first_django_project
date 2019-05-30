from django.db import models


class Track(models.Model):
    track_name = models.CharField(max_length=255, default=None)
    track_duration = models.CharField(max_length=255, default=None)
    album = models.ForeignKey('Album', null=True, on_delete=models.SET_NULL, related_name='tracks')

    def __str__(self):
        return f"{self.track_name}"


class Album(models.Model):
    album_name = models.CharField(max_length=255, default=None)
    year_of_issue = models.PositiveSmallIntegerField()

    music_band = models.ForeignKey('MusicBand', null=True, on_delete=models.SET_NULL, related_name='album')

    def __str__(self):
        return f'{self.album_name}'


class MusicBand(models.Model):
    music_band_name = models.CharField(max_length=255, default=None)
    year_of_foundation = models.PositiveSmallIntegerField()
    music_style = models.CharField(max_length=255, default=None)

    def __str__(self):
        return f'{self.music_band_name}'

# Create your models here.
