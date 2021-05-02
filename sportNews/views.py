from django.shortcuts import render
# from django.http import JsonResponse
from .models import cricketNews as cp
from rest_framework.decorators import api_view
from rest_framework import decorators, permissions
from .serialization import serialization
from django.shortcuts import get_object_or_404 as getobj
# Create your views here.


@decorators.api_view([""])
@decorators.permission_classes([permissions.AllowAny])
def cricketNews(request):
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
        db_table = 'sportNews_cricketNews'
        ordering = ['-timestamp']
        verbose_name = 'cricket News'
        verbose_name_plural = 'cricket News'


@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def delete_post(request):
    # id = int(request.data['id'])
    # postTitle = request.data['post title']
    # obj = getobj(cp, id=id)cricketNews
    # obj.delete()
    return (render(request, 'cricketNews.html'))

  #  return JsonResponse("post deleted", safe=False)
