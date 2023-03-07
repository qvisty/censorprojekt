# censor_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

from censor_app.views import (
    CensorList,
    CensorUpdate,
    SchoolListView,
    SchoolCreate,
    SchoolUpdateView,
    ClassListView,
    ClassCreate,
    ClassUpdateView,
    TeacherListView,
    TeacherCreateView,
    TeacherUpdateView,
    ExamList,
    ExamCreateView,
    ExamUpdateView,
    CensorCreate,
    DashboardView,
)

urlpatterns = [
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("", include("censor_app.urls")),
    # School URLs
    path("schools/", SchoolListView.as_view(), name="school_list"),
    path("schools/create/", SchoolCreate.as_view(), name="school_create"),
    path("schools/<int:pk>/update/", SchoolUpdateView.as_view(), name="school_update"),
    # Class URLs
    path("classes/", ClassListView.as_view(), name="class_list"),
    path("classes/create/", ClassCreate.as_view(), name="class_create"),
    path("classes/<int:pk>/update/", ClassUpdateView.as_view(), name="class_update"),
    # Teacher URLs
    path("teachers/", TeacherListView.as_view(), name="teacher_list"),
    path("teachers/create/", TeacherCreateView.as_view(), name="teacher_create"),
    path(
        "teachers/<int:pk>/update/", TeacherUpdateView.as_view(), name="teacher_update"
    ),
    # Exam URLs
    path("exams/", ExamList.as_view(), name="exam_list"),
    path("exams/create/", ExamCreateView.as_view(), name="exam_create"),
    path("exams/<int:pk>/update/", ExamUpdateView.as_view(), name="exam_update"),
    # Censor URLs
    path("censors/", CensorList.as_view(), name="censor_list"),
    path("censors/create/", CensorCreate.as_view(), name="censor_create"),
    path("censors/<int:pk>/update/", CensorUpdate.as_view(), name="censor_update"),
    path("admin/", admin.site.urls),
]
