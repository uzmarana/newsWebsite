from rest_framework import serializers
from .models import ROBLOX


class serialization(serializers.ModelSerializer):
    class Meta:
        model = ROBLOX

        fields = '__all__'
