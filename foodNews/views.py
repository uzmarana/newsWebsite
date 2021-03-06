from django.shortcuts import render
# from django.http import JsonResponse
from .models import Newfood as nf
from .models import createfood as cf
from rest_framework.decorators import api_view
from rest_framework import decorators, permissions
from .serialization import serialization
from django.shortcuts import get_object_or_404 as getobj
# Create your views here.


@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def Newfood(request):

    render(request, 'Newfood.html')


@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def createfood(request):
    # print(request)

    # postTittle = request.data['postTittle']
    # post = request.data['post']
    # db = cp(postTittle=postTittle, post=post)
    # db.save()
    # data = {"WorldNewsTitile": postTittle, "WorldNews": post}
    # return JsonResponse(data)
    #  return (render(request, 'readpost.html'))

    # @decorators.api_view(["POST"])
    # @decorators.permission_classes([permissions.AllowAny])
    # def readpost(request):
   # data = cp.objects.all()
   # serializer = serialization(data, many=True)
    # return JsonResponse(serializer.data, safe=False)

    class Meta:
        db_table = 'foodNews_Newfood'
        ordering = ['-timestamp']
        verbose_name = 'New food'
        verbose_name_plural = 'New food'


class Meta:
    db_table = 'foodNews_rewiew'
    ordering = ['-timestamp']
    verbose_name = 'rewiew'
    verbose_name_plural = 'rewiew'


@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def delete_post(request):
    # id = int(request.data['id'])
    # postTitle = request.data['post title']
    # obj = getobj(cp, id=id)
    # obj.delete()
    render(request, 'Newfood.html')


#  return JsonResponse("post deleted", safe=False)
# @decorators.api_view(["POST"])
# @decorators.permission_classes([permissions.AllowAny])
def rewiew(request):

    return(render(request, 'rewiew.html'))
