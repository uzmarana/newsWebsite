from rest_framework import serializers
from .models import Newfood
from .models import createfood


class serialization(serializers.ModelSerializer):
    class Meta:
        model = Newfood

        model = createfood
        fields = '__all__'
