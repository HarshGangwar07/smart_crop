from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe

# Create your models here.

class LeafImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    image = models.ImageField(upload_to='leaf_images/')
    date_uploaded = models.DateTimeField(auto_now_add=True) 
    predicted_label = models.CharField(max_length=255, blank=True, null=True)
    confidence_score=models.FloatField(blank=True, null=True)


    def __str__(self):
        return f"Leaf Image {self.id} on {self.date_uploaded}"
    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="100"/>')
        return "No Image"
    image_tag.short_description = 'Image Preview'