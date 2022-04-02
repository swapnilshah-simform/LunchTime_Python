from django.urls import path, include
from .views import MenuView
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('menu', Menuview, basename='menu')
urlpatterns=[
    path('', include(router.urls))
]