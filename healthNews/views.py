from django.shortcuts import render
# from django.http import JsonResponse
from .models import Corona as cp
from rest_framework.decorators import api_view
from rest_framework import decorators, permissions
from .serialization import serialization
from django.shortcuts import get_object_or_404 as getobj
# Create your views here.

# @decorators.api_view(["POST"])
# @decorators.permission_classes([permissions.AllowAny])


def Corona(request):

    # print(request)
    # postTittle = request.data['postTittle']
    # post = request.data['post']
    # db = cp(postTittle=postTittle, post=post)
    # db.save()
    # data = {"WorldNewsTitile": postTittle, "WorldNews": post}
    # return JsonResponse(data)
  #  return (render(request, 'readpost.html'))

    render(request, 'Corona.html')
# @decorators.api_view(["POST"])
# @decorators.permission_classes([permissions.AllowAny])
# def readpost(request):
# data = cp.objects.all()
# serializer = serialization(data, many=True)
# return JsonResponse(serializer.data, safe=False)


class Meta:
    db_table = 'healthNews_Corona'
    ordering = ['-timestamp']
    verbose_name = 'Corona'
    verbose_name_plural = 'Corona'


# @decorators.api_view([""])
# @decorators.permission_classes([permissions.AllowAny])
    #       def createpost(request):


@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def delete_post(request):
    # id = int(request.data['id'])
    # postTitle = request.data['post title']
    # obj = getobj(cp, id=id)
    # obj.delete()
    render(request, 'Corona.html')

  #  return JsonResponse("post deleted", safe=False)
