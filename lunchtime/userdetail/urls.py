from django.urls import path,include
from .views import RegisterView, loginUserPage
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
# router.register('register',RegisterView,basename='register')

# router.register('register',RegisterView,basename='')
urlpatterns = [
    path('', include(router.urls)),

    path('login/', loginUserPage, name='login'),
    path('register/',RegisterView.as_view(),name='register')
]
