from django.urls import path
from. import views

urlpatterns = [

    path('roblox/', views.roblox),
    path('creategame/', views.creategame),



]
