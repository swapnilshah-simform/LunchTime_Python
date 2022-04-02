from django.urls import path, include
from .views import ReviewView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('review',ReviewView, basename = '')
urlpatterns = [
    path('',include(router.urls))
]
