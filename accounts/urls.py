from django.urls import path
from .views import LoginAPIView
from .views import RegisterAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('register/', RegisterAPIView.as_view(), name = 'register')
]
