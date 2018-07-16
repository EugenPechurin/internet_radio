from django import forms

from .models import Station


class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = ('title', 'bit_rate', 'pls', 'm3u', 'url_stream', 'url_station', 'genre')
