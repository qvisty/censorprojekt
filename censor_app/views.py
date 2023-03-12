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


from .models import Skole, Lærer, Eksamen, Censor, Skoleklasse


from django.views.generic.dates import MonthArchiveView

# Crud: Create, Read, Update, Delete, List
# Crud: Create, Detail, Update, Delete, List

#################
###           ###
### Dashboard ###
###           ###
#################


class Dashboard(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Hent alle skoler, prøver og klasser
        eksamener = Eksamen.objects.all()
        skoler = Skole.objects.all()
        skoleklasser = Skoleklasse.objects.all()

        # Tilføj skoler, prøver og klasser til kontekstvariablerne
        context["eksamener"] = eksamener
        context["skoler"] = skoler
        context["skoleklasser"] = skoleklasser

        return context


################
###          ###
###  Censor  ###
###          ###
################


class CensorCreate(CreateView):
    model = Censor
    fields = "__all__"
    template_name = "censor_app/censor_form.html"
    success_url = reverse_lazy("censor_app:censor_list")


class CensorDetail(DetailView):
    model = Censor
    template_name_suffix = "_detail"


class CensorUpdate(UpdateView):
    model = Censor
    template_name = "censor_app/censor_form.html"
    success_url = reverse_lazy("censor_app:censor_list")


class CensorDelete(DeleteView):
    model = Censor
    success_url = reverse_lazy("censor_list")


class CensorList(ListView):
    model = Censor
    template_name = "censor_app/censor_list.html"
    context_object_name = "censorer"


#################
###           ###
###  Eksamen  ###
###           ###
#################


class EksamenCreate(CreateView):
    model = Eksamen
    fields = "__all__"
    success_url = reverse_lazy("eksamen_list")


class EksamenDetail(DetailView):
    model = Eksamen
    template_name = "censor_app/eksamen_detail.html"


class EksamenUpdate(UpdateView):
    model = Eksamen
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("eksamen_list")


class EksamenDelete(DeleteView):
    model = Eksamen
    success_url = reverse_lazy("exam_list")


class EksamenList(ListView):
    model = Eksamen
    context_object_name = "eksamener"


class EksamenMonthArchive(MonthArchiveView):
    queryset = Eksamen.objects.all()
    date_field = "dato"
    allow_future = True


#############
###       ###
### Lærer ###
###       ###
#############


class LærerDetail(DetailView):
    model = Lærer
    template_name_suffix = "_detail"


class LærerList(ListView):
    model = Lærer
    template_name = "censor_app/Lærer_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lærere"] = Lærer.objects.all()
        return context


class LærerUpdate(UpdateView):
    model = Lærer
    fields = ["navn", "email"]
    template_name_suffix = "_detail"
    success_url = reverse_lazy("lærer_list")


class LærerCreate(CreateView):
    model = Lærer
    fields = "__all__"
    template_name = "censor_app/lærer_create.html"


class LærerDelete(DeleteView):
    model = Lærer
    success_url = reverse_lazy("lærer_list")


#############
###       ###
### Skole ###
###       ###
#############


class SkoleList(ListView):
    model = Skole
    template_name = "censor_app/skole_list.html"
    context_object_name = "skoler"


class SkoleUpdate(UpdateView):
    model = Skole
    template_name_suffix = "_update"


class SkoleDelete(DeleteView):
    model = Skole
    success_url = reverse_lazy("skole_list")
    template_name = "censor_app/skole_delete.html"


class SkoleCreate(CreateView):
    model = Skole
    fields = "__all__"
    template_name = "censor_app/skole_form.html"
    success_url = reverse_lazy("skole_list")


class SkoleDetail(DetailView):
    model = Skole
    template_name_suffix = "_detail"


###################
###             ###
### Skoleklasse ###
###             ###
###################


class SkoleklasseDelete(DeleteView):
    model = Skoleklasse
    success_url = reverse_lazy("skoleklasse_list")
    template_name = "censor_app/skoleklasse_delete.html"


class SkoleklasseList(ListView):
    model = Skoleklasse
    template_name = "censor_app/skoleklasse_list.html"
    context_object_name = "skoleklasser"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lærere"] = {}
        for skoleklasse in context["skoleklasser"]:
            context["lærere"][skoleklasse.id] = skoleklasse.lærere.all()
        return context


class SkoleklasseDetail(DetailView):
    model = Skoleklasse
    template_name_suffix = "_detail"


class SkoleklasseCreate(CreateView):
    model = Skoleklasse
    fields = "__all__"


class SkoleklasseUpdate(UpdateView):
    model = Skoleklasse
    template_name = "censor_app/skoleklasse_form.html"

    def get_success_url(self):
        return reverse("skoleklasse_list", kwargs={"pk": self.object.skole.pk})


"""
class SkoleklasseList(ListView):
    model = Skoleklasse
    template_name = "censor_app/skoleklasse_list.html"
    context_object_name = "skoleklasser"

    def get_queryset(self):
        self.skole = get_object_or_404(Skole, id=self.kwargs["skole_id"])
        return Skoleklasse.objects.filter(skole=self.skole)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["skole"] = self.skole
        return context
"""
