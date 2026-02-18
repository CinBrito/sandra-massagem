from django.db import models

class GalleryImage(models.Model):
    title = models.CharField(max_length=150, blank=True)
    image = models.ImageField(upload_to='gallery/')
    alt_text = models.CharField(max_length=200, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title or f"Imagem {self.id}"


class Certification(models.Model):
    title = models.CharField("Título", max_length=200)
    institution = models.CharField("Instituição", max_length=200, blank=True)
    year = models.CharField("Ano", max_length=10, blank=True)

    description = models.TextField("Descrição", blank=True)

    certificate_file = models.FileField(
        "Arquivo (PDF ou imagem)",
        upload_to="certificates/",
        blank=True,
        null=True
    )

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title