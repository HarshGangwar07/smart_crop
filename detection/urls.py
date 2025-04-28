from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_leaf_image, name='upload_leaf_image'),
    path('success/', views.upload_success, name='upload_success'),
]
