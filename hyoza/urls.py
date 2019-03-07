from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('message/', views.answer),
    path('sayhello/', views.sayhello),
    path('showhello/', views.showhello),
    path('showprofile/', views.showprofile),
]
