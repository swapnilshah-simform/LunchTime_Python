from django.shortcuts import render
from .serializer import MenuSerializer
from rest_framework.decorators import api_view
# Create your views here.
from .models import Menu
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializer import MenuSerializer
from rest_framework.viewsets import ModelViewSet

# class MenuView(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = MenuSerializer
@api_view(["POST", "GET"])
def createMenu(request):
    a = request.data.get("menu")
    print(a)
    # b = a[1:len(a)-1]
    # c = b.split(",")
    # d = ",".join(c)
    # print(d)
    # print(d[0])
    d = ",".join([i.strip("''") for i in a.strip('][').split(',')])
    print(d)
    print(d[0])
    menu_obj = Menu.objects.create(menu=str(d), latest_date=request.data.get("time"))
    serializer = MenuSerializer(menu_obj, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)
