from django.shortcuts import render,redirect
from django.core.files.storage import default_storage
from .forms import LeafImageForm
from .models import LeafImage
from .ml_models.predict import predict_disease
from PIL import Image
#from django.contrib.auth.decorators import login_required


# Create your views here.
#@login_required
def upload_leaf_image(request):
    print(f"Default storage backend: {default_storage.__class__.__name__}")  # Debugging
    if request.method == 'POST':
        form = LeafImageForm(request.POST, request.FILES)
        if form.is_valid():
            leaf_image = form.save()
            print(f"Image URL: {leaf_image.image.url}")  # Debugging
            return redirect('upload_success', leaf_id=leaf_image.pk)
        else:
            print("Form is invalid")  # Debugging
    else:
        form = LeafImageForm()
    return render(request, 'detection/upload_image.html', {'form': form})
    
def upload_success(request, leaf_id):
    leaf = LeafImage.objects.get(pk=leaf_id)

    try:
        # ✅ Open image from default storage (S3) using in-memory file
        with default_storage.open(leaf.image.name, 'rb') as f:
            img = Image.open(f)
            img = img.convert("RGB")  # Ensure it's in RGB format
    except Exception as e:
        print("Error opening image:", e)
        img = None
    
    # Run prediction using real model
    if img:
        prediction, confidence = predict_disease(img)  #  Real prediction function
        print(f"Prediction: {prediction}, Confidence: {confidence}")
    else:
        prediction, confidence = None, None

    return render(request, 'detection/upload_success.html', {
        'leaf': leaf,
        'prediction': prediction,
        'confidence': confidence
    })

def leaf_image_list(request):
    images = LeafImage.objects.all().order_by('-date_uploaded')
    for image in images:
        print(image.image.url)
    return render(request,'detection/list_images.html',{'images':images})

