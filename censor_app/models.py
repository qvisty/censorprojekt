from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.db import models


class School(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Exam(models.Model):
    exam_name = models.CharField(max_length=200)
    exam_date = models.DateField(blank=True, null=True, default=timezone.now)
    school_class = models.ForeignKey("SchoolClass", on_delete=models.CASCADE)
    teacher = models.ForeignKey(
        "Teacher", on_delete=models.SET_NULL, blank=True, null=True
    )
    censor = models.ForeignKey(
        "Censor", on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self):
        return self.exam_name

    def get_absolute_url(self):
        return reverse("exam_detail", args=[str(self.id)])


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    # email = models.EmailField()
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="personale",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Censor(models.Model):
    name = models.CharField(max_length=200)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="censors")

    def __str__(self):
        return self.name


class ExamCensor(models.Model):
    exam = models.OneToOneField(
        Exam, on_delete=models.CASCADE, related_name="exam_censor"
    )
    censor = models.ForeignKey(
        Censor, on_delete=models.CASCADE, related_name="exam_censors"
    )

    def __str__(self):
        return f"{self.exam} - {self.censor}"


class MissingData(models.Model):
    class_name = models.CharField(max_length=200)
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="missing_datas"
    )
    date = models.DateField(null=True, blank=True)
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name="missing_datas",
        null=True,
        blank=True,
    )
    censor = models.ForeignKey(
        Censor,
        on_delete=models.CASCADE,
        related_name="missing_datas",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.class_name} - {self.school}"


class SchoolClass(models.Model):
    name = models.CharField(max_length=50)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("class_detail", kwargs={"pk": self.pk})
