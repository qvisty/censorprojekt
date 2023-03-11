from django.db import models
from django.urls import reverse
from django.utils import timezone


class Skole(models.Model):
    navn = models.CharField(max_length=200)
    addresse = models.CharField(max_length=200)

    def __str__(self):
        return self.navn


class Eksamen(models.Model):
    navn = models.CharField(max_length=200)
    dato = models.DateField(blank=True, null=True, default=timezone.now)
    skoleklasse = models.ForeignKey("Skoleklasse", on_delete=models.CASCADE)
    lærer = models.ForeignKey("Lærer", on_delete=models.SET_NULL, blank=True, null=True)
    censor = models.ForeignKey(
        "Censor", on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return self.fag

    def get_absolute_url(self):
        return reverse("exam_detail", args=[str(self.id)])


class Lærer(models.Model):
    navn = models.CharField(max_length=200)
    email = models.EmailField()
    skole = models.ForeignKey(
        Skole,
        on_delete=models.CASCADE,
        related_name="personale",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.navn


class Censor(models.Model):
    navn = models.CharField(max_length=200)
    skole = models.ForeignKey(Skole, on_delete=models.CASCADE, related_name="censorer")

    def __str__(self):
        return self.navn


class EksamensCensor(models.Model):
    eksamen = models.OneToOneField(
        Eksamen, on_delete=models.CASCADE, related_name="_eksamen"
    )
    censor = models.ForeignKey(Censor, on_delete=models.CASCADE, related_name="_censor")

    def __str__(self):
        return f"{self.eksamen} - {self.censor}"


class Skoleklasse(models.Model):
    navn = models.CharField(max_length=50)
    skole = models.ForeignKey(Skole, on_delete=models.CASCADE)
    lærere = models.ManyToManyField(Lærer, blank=True)

    def __str__(self):
        return self.navn

    def get_absolute_url(self):
        return reverse("class_detail", kwargs={"pk": self.pk})
