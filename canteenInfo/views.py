from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from .serlizers import CanteenInfoSerializer
from rest_framework.viewsets import ModelViewSet


class CanteenInfoView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CanteenInfoSerializer