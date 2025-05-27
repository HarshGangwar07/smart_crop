from rest_framework import serializers
from .models import LeafImage

class LeafImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeafImage
        fields = '__all__'
