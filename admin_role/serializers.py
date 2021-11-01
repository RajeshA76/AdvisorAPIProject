from rest_framework import serializers
from .models import AdvisorModel

class AdvisorSerializer(serializers.ModelSerializer):

    class Meta:
        model = AdvisorModel
        fields = ['AdvisorName','AdvisorPhotoUrl']

