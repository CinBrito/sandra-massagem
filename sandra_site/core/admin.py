from django.contrib import admin
from .models import GalleryImage
from .models import Certification
from .models import Service

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'order', 'created_at')
    list_editable = ('order',)
    search_fields = ('title',)

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("title", "section", "institution", "year", "order")
    list_filter = ("section",)
    search_fields = ("title", "institution")
    ordering = ("section", "order")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "order", "is_active", "is_featured")
    list_editable = ("category", "order", "is_active", "is_featured")
    search_fields = ("title",)
    ordering = ("category", "order", "title")
    list_filter = ("category", "is_active", "is_featured")

    def preview(self, obj):
        if obj.certificate_image:
            return format_html(
                '<img src="{}" width="50" style="border-radius:4px;" />',
                obj.certificate_image.url
            )
        return "-"
