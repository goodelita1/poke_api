from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index),
    #path('about/', views.about),
    path('about/', views.get_name)
]