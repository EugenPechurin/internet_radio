from django.shortcuts import render, redirect
from .models import Station
from subprocess import call


def index(request):
    stations = Station.objects.all()
    context = {'stations': stations}
    return render(request, 'stations.html', context)


def crawler(request):
    # run crawler
    call("scrapy crawl stations_list", cwd="/home/eugen/PycharmProjects/internet-radio/crawler", shell=True)
    return redirect('/')


def delete_all(request):
    Station.objects.all().delete()
    return redirect('/')
