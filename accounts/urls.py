from django.urls import path
from .views import RegisterAPIView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)


urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name = 'register'),
    path('login/', TokenObtainPairView.as_view(), name = 'jwt_login'),
    path('refresh/',TokenRefreshView.as_view(), name = 'jwt_refresh'),
    path('verify/', TokenVerifyView.as_view(),name ='jwt_verfiy'),
]
