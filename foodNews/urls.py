from django.urls import path
from. import views

urlpatterns = [

    path('Newfood/', views.Newfood),
    path('createpost/', views.createpost)


]
