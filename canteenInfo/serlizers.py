from rest_framework import serializers
from .models import CanteenInfo


class CanteenInfoSerializer(serializers.ModelSerializer): 
    class Meta:
        model = CanteenInfo
        field = '__all__'
