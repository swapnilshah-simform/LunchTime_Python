from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Profile
from rest_framework.views import APIView

from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from rest_framework import generics
from django.contrib.auth import login


# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegisterSerializer


class RegisterView(APIView):
    def post(self, request):
        data = request.data
        reg_serializer = RegisterSerializer(data=data)
        if reg_serializer.is_valid():
            password = reg_serializer.validated_data.get('password')
            reg_serializer.validated_data['password']=make_password(password)
            new_user = reg_serializer.save()
            if new_user:
                return Response(new_user.id)
        return Response(reg_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST", "GET"])
def loginUserPage(request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email = serializer.validated_data['email']
    password = serializer.validated_data['password']

    try:
        user = User.objects.get(email=email)
        if user.check_password(password):
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    except BaseException as e:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def createProfile(request):
    user = User.objects.get(id=request.data.get("pk"))
    profile = Profile.objects.create(user=user, department=request.data.get("department"), trainee_or_employee=request.data.get('trainee_or_employee'))
    serializer = ProfileSerializer(profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


