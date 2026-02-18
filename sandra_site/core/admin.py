from django.contrib import admin
from .models import GalleryImage
from .models import Certification

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'order', 'created_at')
    list_editable = ('order',)
    search_fields = ('title',)

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("title", "institution", "year", "order")
    list_editable = ("order",)
