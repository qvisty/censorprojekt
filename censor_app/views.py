# censor_app/views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView, UpdateView, DeleteView  # CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView

from .models import School, Teacher, Exam, Censor, ExamCensor, MissingData, SchoolClass


class SchoolListView(ListView):
    model = School
    template_name = "censor_app/school_list.html"


class SchoolCreate(CreateView):
    model = School
    fields = ["name", "address", "phone_number", "email"]
    template_name = "censor_app/form.html"
    success_url = reverse_lazy("school_list")


class SchoolUpdateView(UpdateView):
    model = School
    fields = ["name"]
    template_name = "censor_app/school_update.html"


class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy("school_list")
    template_name = "censor_app/school_delete.html"


class TeacherListView(ListView):
    model = Teacher
    template_name = "censor_app/teacher_list.html"


class TeacherCreateView(CreateView):
    model = Teacher
    fields = ["name", "school"]
    template_name = "censor_app/teacher_create.html"


class DashboardView(TemplateView):
    template_name = "dashboard.html"


class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = ["name", "email"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("teacher_list")


class ClassListView(ListView):
    model = SchoolClass
    template_name = "censor_app/class_list.html"
    context_object_name = "class_list"

    def get_queryset(self):
        self.school = get_object_or_404(School, id=self.kwargs["school_id"])
        return SchoolClass.objects.filter(school=self.school)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["school"] = self.school
        return context


class SchoolClassListView(ListView):
    model = SchoolClass
    template_name = "censor_app/school_class_list.html"
    context_object_name = "school_classes"

    def get_queryset(self):
        self.school = get_object_or_404(School, id=self.kwargs["pk"])
        return SchoolClass.objects.filter(school=self.school)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["school"] = self.school
        return context


class CensorList(ListView):
    model = Censor
    template_name = "censor_app/censor_list.html"
    context_object_name = "censors"


class CensorCreate(CreateView):
    model = Censor
    template_name = "censor_app/censor_form.html"
    fields = "__all__"
    success_url = reverse_lazy("censor_app:censor_list")


class CensorUpdate(UpdateView):
    model = Censor
    template_name = "censor_app/censor_form.html"
    fields = "__all__"
    success_url = reverse_lazy("censor_app:censor_list")


class ClassCreate(CreateView):
    model = SchoolClass
    fields = ["name"]


class ClassUpdateView(UpdateView):
    model = SchoolClass
    fields = ("name",)
    template_name = "censor_app/class_form.html"

    def get_success_url(self):
        return reverse("school_class_list", kwargs={"pk": self.object.school.pk})


class ExamList(ListView):
    model = Exam


class ExamUpdate(UpdateView):
    model = Exam
    fields = ["exam_name", "exam_date", "school_class", "teacher", "censor"]


class ExamDelete(DeleteView):
    model = Exam
    success_url = reverse_lazy("exam_list")


class ExamCreate(CreateView):
    model = Exam
    fields = ["exam_name", "exam_date", "school_class", "teacher", "censor"]
    success_url = reverse_lazy("exam_list")


class ExamCreateView(CreateView):
    model = Exam
    fields = ["class_name", "subject", "date"]
    template_name_suffix = "_create_form"
    success_url = reverse_lazy("censor_list")


class ExamUpdateView(UpdateView):
    model = Exam
    fields = ["class_name", "subject", "date"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("censor_list")
