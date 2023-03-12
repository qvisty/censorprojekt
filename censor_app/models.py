from django.db import models
from django.urls import reverse
from django.utils import timezone


class Skole(models.Model):
    navn = models.CharField(max_length=200)
    adresse = models.CharField(max_length=200)

    def __str__(self):
        return self.navn

    class Meta:
        verbose_name_plural = "Skoler"


class Eksamen(models.Model):
    navn = models.CharField(max_length=200)  # fag
    dato = models.DateField(blank=True, null=True, default=timezone.now)
    skoleklasse = models.ForeignKey("Skoleklasse", on_delete=models.CASCADE)
    lærer = models.ForeignKey("Lærer", on_delete=models.SET_NULL, blank=True, null=True)
    censor = models.ForeignKey(
        "Censor", on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return self.navn

    def get_absolute_url(self):
        return reverse("exam_detail", args=[str(self.id)])

    class Meta:
        verbose_name_plural = "Eksamener"


class Lærer(models.Model):
    navn = models.CharField(max_length=200)
    email = models.EmailField(blank=True, null=True)
    skole = models.ForeignKey(
        Skole,
        on_delete=models.CASCADE,
        related_name="personale",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.navn

    class Meta:
        verbose_name_plural = "Lærere"


class Censor(models.Model):
    navn = models.CharField(max_length=200)
    fag = models.CharField(max_length=200)
    skole = models.ForeignKey(Skole, on_delete=models.CASCADE, related_name="censorer")
    email = models.EmailField()

    def __str__(self):
        return self.navn

    class Meta:
        verbose_name_plural = "Censorer"


class Skoleklasse(models.Model):
    navn = models.CharField(max_length=50)
    skole = models.ForeignKey(Skole, on_delete=models.CASCADE)
    lærere = models.ManyToManyField(Lærer, blank=True, related_name="klasser")

    def __str__(self):
        return self.navn

    def get_absolute_url(self):
        return reverse("klasse_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name_plural = "Skoleklasser"
