from django.urls import path,include
from .views import RegisterView
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
# router.register('register',RegisterView,basename='')
urlpatterns = [
    path('register/',RegisterView.as_view(),name='register')
]
