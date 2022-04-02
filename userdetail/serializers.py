from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']
    def validate_email(self, email):
        if not email.endswith("@simformsolutions.com"):
            raise serializers.ValidationError('enter valid email address')
        return email
