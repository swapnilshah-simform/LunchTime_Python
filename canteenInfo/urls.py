from django.urls import path, include
from .views import CanteenInfoView
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('canteenInfo',CanteenInfoView,basename='canteenInfo')
urlpatterns=[
    path('', include(router.urls)),
]