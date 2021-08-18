from GamingNews.views import creategame, roblox
from rest_framework import serializers
from .models import roblox


class serialization(serializers.ModelSerializer):
    class Meta:
        model = roblox

        model = creategame
        fields = '__all__'
