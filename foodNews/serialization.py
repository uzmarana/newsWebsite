from rest_framework import serializers
from .models import Newfood


class serialization(serializers.ModelSerializer):
    class Meta:
        model = Newfood

        fields = '__all__'
