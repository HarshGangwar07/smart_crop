from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_leaf_image, name='upload_leaf_image'),
    path('success/', views.upload_success, name='upload_success'),
    path('list/', views.leaf_image_list,name='leaf_image_list')
]
