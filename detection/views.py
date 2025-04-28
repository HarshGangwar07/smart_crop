from django.shortcuts import render,redirect
from .forms import LeafImageForm
from .models import LeafImage
#from django.contrib.auth.decorators import login_required


# Create your views here.
#@login_required
def upload_leaf_image(request):
    if request.method == 'POST':
        form = LeafImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')
    else:
        form = LeafImageForm()
    return render(request, 'detection/upload_image.html', {'form':form})
    
def upload_success(request):
    return render(request, 'detection/upload_success.html')