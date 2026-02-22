from django.shortcuts import render
from .models import GalleryImage
from .models import Certification
from .models import Service
from .models import Testimonial

def home(request):
    services = Service.objects.filter(is_active=True, is_featured=True)
    testimonials = Testimonial.objects.all()
    return render(request, "core/index.html", {
        "services": services,
        "testimonials": testimonials,
    })

def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, "core/gallery.html", {
        "images": images
    })

def certifications(request):
    certifications = Certification.objects.all()

    context = {
        "formacao": certifications.filter(section="formacao"),
        "especializacoes": certifications.filter(section="especializacoes"),
        "experiencia": certifications.filter(section="experiencia"),
        "eventos": certifications.filter(section="eventos"),
    }
    return render(request, "core/certifications.html", context)


def services(request):
    services = Service.objects.filter(is_active=True)
    return render(request, "core/services.html", {
        "massagens": services.filter(category="massagens"),
        "experiencias": services.filter(category="experiencias"),
    })
