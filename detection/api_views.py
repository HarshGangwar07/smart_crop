from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from django.core.files.storage import default_storage
from .models import LeafImage
from .serializers import LeafImageSerializer
from .ml_models.predict import predict_disease
from PIL import Image
import logging

# Upload & List leaf images
class LeafImageListCreateView(generics.ListCreateAPIView):
    queryset = LeafImage.objects.all().order_by('-date_uploaded')  
    serializer_class = LeafImageSerializer
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        instance = serializer.save()
        print(f"Image URL: {instance.image.url}")  # Optional debug log


# Predict disease from an uploaded image
class PredictDiseaseView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, *args, **kwargs):
        image_file = request.FILES.get('image')
        if not image_file:
            return Response({"error": "No image provided"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Save image temporarily (S3-compatible if configured)
            image_path = default_storage.save(image_file.name, image_file)

            # Open the image from storage
            with default_storage.open(image_path, 'rb') as f:
                img = Image.open(f).convert("RGB")

            # Run prediction
            prediction, confidence = predict_disease(img)

            return Response({
                "prediction": prediction,
                "confidence": confidence,
                "image_url": default_storage.url(image_path)
            })
        except Exception as e:
            logging.exception("Error during disease prediction")
        


# Retrieve, update, delete individual image by ID
class LeafImageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = LeafImage.objects.all()
    serializer_class = LeafImageSerializer
