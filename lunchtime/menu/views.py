from django.shortcuts import render
from .serializer import MenuSerializer
from rest_framework.decorators import api_view
# Create your views here.
from .models import Menu
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializer import MenuSerializer
from rest_framework.viewsets import ModelViewSet
import json
from types import SimpleNamespace


# class MenuView(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = MenuSerializer
@api_view(["POST", "GET"])
def createMenu(request):
    a = request.data.get("menu")
    print(a)
    a = a[1:len(a) - 1]
    d = eval(a)

    print(d)
    b = 0
    c = {}
    for i in d:
        c[b] = i
        b += 1
    print(c)
    # print(a[0])
    print(c[0])
    z = c[0]
    print(z)

    menu_obj = Menu.objects.create(menu=z, latest_date=request.data.get("time"))
    print(menu_obj)
    serializer = MenuSerializer(menu_obj, data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response(c)
    return Response(serializer.errors)


@api_view(["GET"])
def getMenu(request,pk):
    data = Menu.objects.filter(latest_date=pk).first()
    a = eval(data.menu)
    b = {}
    c = 0
    for i in a:
        b[c] = i
        c += 1
    serializer = MenuSerializer(data)
    return Response(b)
