from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('galeria/', views.gallery, name='gallery'),
    path("certificacoes/", views.certifications, name="certifications"),
]
