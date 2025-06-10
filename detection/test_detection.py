import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
import io

@pytest.mark.django_db
def test_detection_creat():
    img = Image.new('RGB', (128, 128), color='green')
    buf = io.BytesIO()
    img.save(buf, format='JPEG')
    buf.seek(0)
    image_file = SimpleUploadedFile("test_image.jpg", buf.read(), content_type="image/jpeg")
    client = APIClient()
    url = reverse('leafimage-list-create')
    response = client.post(reverse('leafimage-list-create'), {'image': image_file}, format='multipart')
    assert response.status_code == status.HTTP_201_CREATED
    assert 'id' in response.data
    assert 'image' in response.data

