from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Profile

from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from rest_framework import generics
from django.contrib.auth import login


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


@api_view(["POST", "GET"])
def loginUserPage(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.validated_data['email']
    password = serializer.validated_data['password']

    try:
        user = User.objects.get(email=email)
        if user.check_password(password):
            return Response(user.profile.profile_id)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    except BaseException as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def createProfile(request):
    user = User.objects.get(id=request.data.get("pk"))
    profile = Profile.objects.create(user=user, department=request.data.get("department"), trainee_or_employee=request.data.get('trainee_or_employee'))
    serializer = ProfileSerializer(profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
