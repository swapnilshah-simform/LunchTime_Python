from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.viewsets import ModelViewSet


class RegisterView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer