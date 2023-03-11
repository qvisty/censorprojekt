# censor_app/views.py
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView
from django.views.generic import (
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
    TemplateView,
)  # CreateView
from django.shortcuts import render, redirect, get_object_or_404


from .models import Skole, Lærer, Eksamen, Censor, EksamensCensor, Skoleklasse


from django.views.generic.dates import MonthArchiveView


class EksamenMonthArchive(MonthArchiveView):
    queryset = Eksamen.objects.all()
    date_field = "dato"
    allow_future = True


class SkoleList(ListView):
    model = Skole
    template_name = "censor_app/school_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["schools"] = Skole.objects.all()
        return context


class SkoleCreate(CreateView):
    model = Skole
    # fields = ["navn", "addresse"]
    template_name = "censor_app/form.html"
    success_url = reverse_lazy("school_list")


class SkoleDetail(DetailView):
    model = Skole
    # fields = ["navn"]
    template_name_suffix = "_detail"


class CensorDetail(DetailView):
    model = Censor
    # fields = ["navn"]
    template_name_suffix = "_detail"

class LærerDetail(DetailView):
    model = Lærer
    # fields = ["navn"]
    template_name_suffix = "_detail"

class SkoleUpdate(UpdateView):
    model = Skole
    # fields = ["navn"]
    template_name_suffix = "_update"


class SkoleDelete(DeleteView):
    model = Skole
    success_url = reverse_lazy("school_list")
    template_name = "censor_app/school_delete.html"

class SkoleklasseDelete(DeleteView):
    model = Skoleklasse
    success_url = reverse_lazy("skoleklasse_list")
    template_name = "censor_app/skoleklasse_delete.html"

class LærerList(ListView):
    model = Lærer
    template_name = "censor_app/Lærer_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teachers"] = Lærer.objects.all()
        return context


class LærerCreate(CreateView):
    model = Lærer
    # fields = ["navn", "skole"]
    template_name = "censor_app/Lærer_create.html"


class Dashboard(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Hent alle skoler, prøver og klasser
        eksamener = Eksamen.objects.all()
        skoler = Skole.objects.all()
        klasser = Skoleklasse.objects.all()

        # Tilføj skoler, prøver og klasser til kontekstvariablerne
        context["eksamener"] = eksamener
        context["skoler"] = skoler
        context["klasser"] = klasser

        return context


class LærerUpdate(UpdateView):
    model = Lærer
    # fields = ["navn", "skole"]
    template_name_suffix = "_detail"
    success_url = reverse_lazy("Lærer_list")


class SkoleklasseList(ListView):
    model = Skoleklasse
    template_name = "censor_app/class_list.html"
    context_object_name = "class_list"

    def get_queryset(self):
        self.skole = get_object_or_404(Skole, id=self.kwargs["school_id"])
        return Skoleklasse.objects.filter(skole=self.skole)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["school"] = self.skole
        return context


class SkoleklasseList(ListView):
    model = Skoleklasse
    template_name = "censor_app/school_class_list.html"
    context_object_name = "school_classes"


class SkoleklasseDetail(DetailView):
    model = Skoleklasse
    # fields = ["navn"]
    template_name_suffix = "_detail"


class CensorList(ListView):
    model = Censor
    template_name = "censor_app/censor_list.html"
    context_object_name = "censors"


class CensorCreate(CreateView):
    model = Censor
    template_name = "censor_app/censor_form.html"
    # fields = "__all__"
    success_url = reverse_lazy("censor_app:censor_list")


class CensorUpdate(UpdateView):
    model = Censor
    template_name = "censor_app/censor_form.html"
    # fields = "__all__"
    success_url = reverse_lazy("censor_app:censor_list")


class SkoleklasseCreate(CreateView):
    model = Skoleklasse
    # fields = ["navn"]


class SkoleklasseUpdate(UpdateView):
    model = Skoleklasse
    # fields = ("navn",)
    template_name = "censor_app/class_form.html"

    def get_success_url(self):
        return reverse("school_class_list", kwargs={"pk": self.object.skole.pk})


class EksamenList(ListView):
    model = Eksamen
    context_object_name = "exams"


class EksamenUpdate(UpdateView):
    model = Eksamen
    # fields = ["navn", "dato", "skoleklasse", "lærer", "censor"]


class EksamenDelete(DeleteView):
    model = Eksamen
    success_url = reverse_lazy("exam_list")


class CensorDelete(DeleteView):
    model = Censor
    success_url = reverse_lazy("censor_list")

class LærerDelete(DeleteView):
    model = Lærer
    success_url = reverse_lazy("lærer_list")

class EksamenCreate(CreateView):
    model = Eksamen
    # fields = ["navn", "dato", "skoleklasse", "lærer", "censor"]
    success_url = reverse_lazy("exam_list")



class EksamenUpdate(UpdateView):
    model = Eksamen
    # fields = ["class_name", "subject", "date"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("censor_list")


class EksamenDetail(DetailView):
    model = Eksamen
    template_name = "censor_app/exam_detail.html"
