from django.urls import path, include
from .views import RegisterView, loginUserPage, createProfile, password_reset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('register',RegisterView,basename='register')

# router.register('register',RegisterView,basename='')
urlpatterns = [
    path('', include(router.urls)),

    path('login/', loginUserPage, name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', createProfile, name='profile'),
    path('reset/', password_reset, name='reset_password'),
]
