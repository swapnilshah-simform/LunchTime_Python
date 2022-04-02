from rest_framework import serializers
from .models import Reviews

class ReviewsService(serializers.ModelSerializer):
    class Meta:
        model = reviews
        field = '__all__'


    