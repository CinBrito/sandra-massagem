from django.core.exceptions import ValidationError
from django.db import models


class GalleryImage(models.Model):
    title = models.CharField(max_length=150, blank=True, verbose_name="Título")
    image = models.ImageField(upload_to="gallery/", verbose_name="Imagem")
    alt_text = models.CharField(max_length=200, blank=True, verbose_name="Texto alternativo")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    order = models.PositiveIntegerField(default=0, verbose_name="Ordem")

    class Meta:
        ordering = ["order", "-created_at"]
        verbose_name = "Imagem da Galeria"
        verbose_name_plural = "Galeria de Imagens"

    def __str__(self):
        return self.title or f"Imagem {self.id}"


class Service(models.Model):
    CATEGORY_CHOICES = [
        ("massagens", "Massagens"),
        ("experiencias", "Experiências"),
    ]

    title = models.CharField(max_length=120, verbose_name="Título")
    description = models.TextField(verbose_name="Descrição")
    image = models.ImageField(upload_to="services/", verbose_name="Imagem")
    alt_text = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Texto alternativo",
    )
    order = models.PositiveIntegerField(default=0, verbose_name="Ordem")
    is_active = models.BooleanField(default=True, verbose_name="Ativo")
    is_featured = models.BooleanField(default=False, verbose_name="Destaque")
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default="massagens",
        verbose_name="Categoria",
    )

    class Meta:
        ordering = ["category", "order", "title"]
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

    def __str__(self):
        return self.title

    def clean(self):
        super().clean()
        if self.is_featured:
            existing = Service.objects.filter(is_featured=True)
            if self.pk:
                existing = existing.exclude(pk=self.pk)
            if existing.count() >= 3:
                raise ValidationError({
                    "is_featured": "Já existem 3 serviços em destaque. Desmarque um para adicionar outro."
                })


class Certification(models.Model):
    SECTION_CHOICES = [
        ("formacao", "Formação Profissional"),
        ("especializacoes", "Especializações"),
        ("experiencia", "Experiência Profissional"),
        ("eventos", "Experiências em Evento"),
    ]

    section = models.CharField(
        max_length=30,
        choices=SECTION_CHOICES,
        verbose_name="Seção",
        default="formacao",
    )

    title = models.CharField(max_length=200, verbose_name="Título")

    institution = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Instituição",
    )

    year = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Ano",
    )

    description = models.TextField(
        blank=True,
        verbose_name="Descrição"
    )

    # 🆕 NOVO CAMPO (opcional)
    certificate_image = models.ImageField(
        upload_to="certificates/",
        blank=True,
        null=True,
        verbose_name="Imagem do certificado"
    )

    order = models.PositiveIntegerField(
        default=0,
        help_text="Ordem dentro da seção",
        verbose_name="Ordem",
    )

    class Meta:
        ordering = ["section", "order", "-year"]
        verbose_name = "Certificação"
        verbose_name_plural = "Certificações"

    def __str__(self):
        return f"{self.get_section_display()} — {self.title}"
