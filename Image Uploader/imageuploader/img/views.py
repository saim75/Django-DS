from django.shortcuts import render
from .forms import ImageUploadForm
from .models import Image


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})

def display_images(request):
    images = Image.objects.all()
    return render(request, 'display.html', {'images': images})

def image_detail(request, image_id):
    image = Image.objects.get(id=image_id)
    return render(request, 'detail.html', {'image': image})
