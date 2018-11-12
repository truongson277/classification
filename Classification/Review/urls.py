from django.urls import path
from . import views

urlpatterns = [

    path('home', views.index),
    path('input', views.data),
    path('save', views.save_data)

]