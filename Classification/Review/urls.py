from django.urls import path
from . import views

urlpatterns = [

    path('home', views.index),
    path('input', views.data),
    path('save', views.save_data),
    path('predict', views.predict_review),
    path('save-predict', views.save_predict)

]