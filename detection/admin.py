from django.contrib import admin
from .models import LeafImage

# Register your models here.



@admin.register(LeafImage)

class LeafImageAdmin(admin.ModelAdmin):
    list_display = ('id','image_tag', 'date_uploaded')
    readonly_fields=('image_tag',)
    