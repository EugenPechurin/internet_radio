from django.urls import path
from . import views

urlpatterns = [
    path('update/', views.crawler),
    path('delete_all/', views.delete_all),
    path('', views.index)
]