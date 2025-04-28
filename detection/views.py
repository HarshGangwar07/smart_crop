from django.shortcuts import render,redirect
from .forms import LeafImageForm
from .models import LeafImage
from .utils import dummy_predict
#from django.contrib.auth.decorators import login_required


# Create your views here.
#@login_required
def upload_leaf_image(request):
    if request.method == 'POST':
        form = LeafImageForm(request.POST, request.FILES)
        if form.is_valid():
            leaf_image = form.save() #Save the uploaded image first
            
            #Get the image path
            image_path = leaf_image.image.path

            #Get dummy prediction
            label, confidence = dummy_predict(image_path)

            #Save the prediction to this leaf_image instance
            leaf_image.predicted_label = label
            leaf_image.confidence_score = confidence
            leaf_image.save()

            return redirect('upload_success')
    else:
        form = LeafImageForm()
    return render(request, 'detection/upload_image.html', {'form':form})
    
def upload_success(request):
    return render(request, 'detection/upload_success.html')

def leaf_image_list(request):
    images = LeafImage.objects.all().order_by('-date_uploaded')
    return render(request,'detection/list_images.html',{'images':images})