from rest_framework import serializers
from .models import Newfood
from .models import createpost


class serialization(serializers.ModelSerializer):
    class Meta:
        model = Newfood
        model = createpost
        fields = '__all__'
