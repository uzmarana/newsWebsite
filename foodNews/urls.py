from django.urls import path
from. import views

urlpatterns = [

    path('Newfood/', views.Newfood),
    path('createfood/', views.createfood),
    path('rewiew/', views.rewiew),



]
