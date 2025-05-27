from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import default_storage
from .forms import LeafImageForm
from .models import LeafImage
from .ml_models.predict import predict_disease
from PIL import Image

# Upload form using HTML template
def upload_leaf_image(request):
    if request.method == 'POST':
        form = LeafImageForm(request.POST, request.FILES)
        if form.is_valid():
            leaf_image = form.save()
            return redirect('upload_success', leaf_id=leaf_image.pk)
    else:
        form = LeafImageForm()
    return render(request, 'detection/upload_image.html', {'form': form})

# Success page with prediction results
def upload_success(request, leaf_id):
    leaf = get_object_or_404(LeafImage, pk=leaf_id)

    try:
        with default_storage.open(leaf.image.name, 'rb') as f:
            img = Image.open(f)
            img = img.convert("RGB")
            prediction, confidence = predict_disease(img)
    except Exception as e:
        prediction, confidence = None, None
        print("Prediction Error:", e)

    return render(request, 'detection/upload_success.html', {
        'leaf': leaf,
        'prediction': prediction,
        'confidence': confidence
    })

# List all uploaded images
def leaf_image_list(request):
    images = LeafImage.objects.all().order_by('-date_uploaded')
    return render(request, 'detection/list_images.html', {'images': images})
