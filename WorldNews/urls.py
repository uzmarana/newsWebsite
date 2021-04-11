from django.urls import path
from . import views

urlpatterns = [

    path('readpost/', views.readpost),
    path('createpost/', views.createpost),
    # path('deletepost/', views.deletepost, name='deletepost'),
    path('deletepost/', views.delete_post)

]
