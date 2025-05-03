from django.shortcuts import render,redirect
from django.core.files.storage import default_storage
from .forms import LeafImageForm
from .models import LeafImage
from .utils import dummy_predict
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
        image_url = leaf.image.url
    except NotImplementedError:
        # fallback if url is not supported
        image_url = default_storage.url(leaf.image.name)
    except Exception as e:
        print("Error getting image URL:", e)
        image_url = None

    # Debug: ensure image_url is usable
    print("Image URL for prediction:", image_url)

    if image_url:
        prediction, confidence = dummy_predict(image_url)
        print(f"Prediction: {prediction}, Confidence: {confidence}")  # Debugging
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

