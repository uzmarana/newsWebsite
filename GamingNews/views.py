from django.shortcuts import render
# from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework import decorators, permissions
# from .serialization import serialization
from django.shortcuts import get_object_or_404 as getobj


@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def roblox(request):
    return (render(request, 'roblox.html'))


@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def creategame(request):

    class Meta:
        db_table = 'GamingNews_roblox'
        ordering = ['-timestamp']
        verbose_name = 'roblox'
        verbose_name_plural = 'roblox'


@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def delete_post(request):

    render(request, 'roblox')
