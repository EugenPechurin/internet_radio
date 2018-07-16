# -*- coding: utf-8 -*-
from scrapy_djangoitem import DjangoItem
from station.models import Station, Genres


class StationItem(DjangoItem):
    django_model = Station


class GenreItem(DjangoItem):
    django_model = Genres
