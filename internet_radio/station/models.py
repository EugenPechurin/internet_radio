from django.db import models
from django.utils import timezone


class Genres(models.Model):
    title = models.CharField(max_length=200)


class Station(models.Model):

    title = models.CharField(max_length=200)
    bit_rate = models.CharField(max_length=10)
    pls = models.CharField(max_length=200)
    m3u = models.CharField(max_length=200)
    url_stream = models.URLField(max_length=200)
    url_station = models.URLField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    genre = models.ManyToManyField(Genres)

    def __str__(self):
        return self.title



