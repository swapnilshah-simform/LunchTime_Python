from django.urls import path,include
from .views import UpdateCounter, GetCounter
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
# router.register('register',RegisterView,basename='register')

# router.register('register',RegisterView,basename='')
urlpatterns = [
    path('counter/<str:pk>/', UpdateCounter, name='counter'),
    path('counter/', GetCounter, name='getcounter'),
]