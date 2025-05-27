from django.urls import path
from . import views
from .api_views import LeafImageListCreateView, LeafImageDetailView, PredictDiseaseView 

urlpatterns = [
    # Template-based views
    path('upload/', views.upload_leaf_image, name='upload_leaf_image'),
    path('success/<int:leaf_id>/', views.upload_success, name='upload_success'),
    path('list/', views.leaf_image_list, name='leaf_image_list'),

    # ✅ DRF API views
    path('api/images/', LeafImageListCreateView.as_view(), name='leafimage-list-create'),
    path('api/images/<int:pk>/', LeafImageDetailView.as_view(), name='leafimage-detail'),
    path('api/predict/', PredictDiseaseView.as_view(), name='predict-disease'),
]
