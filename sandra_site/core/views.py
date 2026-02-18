from django.shortcuts import render
from .models import GalleryImage
from .models import Certification

def home(request):
    return render(request, 'core/index.html')

def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, "core/gallery.html", {
        "images": images
    })

def certifications(request):
    certifications = Certification.objects.all()
    return render(request, "core/certifications.html", {
        "certifications": certifications
    })