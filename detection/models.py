from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class LeafImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='leaf_images/')
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Leaf Image {self.id} on {self.date_uploaded}"
