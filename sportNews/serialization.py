from rest_framework import serializers
from .models import cricketNews


class serialization(serializers.ModelSerializer):
    class Meta:

        model = cricketNews
        fields = '__all__'
