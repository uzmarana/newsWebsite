from rest_framework import serializers
from .models import Corona


class serialization(serializers.ModelSerializer):
    class Meta:
        model = Corona

        fields = '__all__'
