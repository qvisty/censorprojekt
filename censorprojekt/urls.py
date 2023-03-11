# censor_project/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

from censor_app.views import (
    Dashboard,
    CensorCreate,
    CensorDetail,
    CensorDelete,
    CensorList,
    CensorUpdate,
    LærerCreate,
    LærerDetail,
    LærerDelete,
    LærerList,
    LærerUpdate,
    SkoleCreate,
    SkoleDelete,
    SkoleDetail,
    SkoleList,
    SkoleUpdate,
    SkoleklasseCreate,
    SkoleklasseDetail,
    SkoleklasseDelete,
    SkoleklasseList,
    SkoleklasseUpdate,
    EksamenList,
    EksamenCreate,
    EksamenDelete,
    EksamenDetail,
    EksamenUpdate,
    EksamenMonthArchive,
)

urlpatterns = [
    path("", include("censor_app.urls")),
    # School URLs
    path("schools/<int:pk>/update/", SkoleUpdate.as_view(), name="school_update"),
    path("schools/create/", SkoleCreate.as_view(), name="school_create"),
    path("schools/<int:pk>/", SkoleDetail.as_view(), name="skole_detail"),
    path("schools/", SkoleList.as_view(), name="school_list"),
    # Class URLs
    path("classes/", SkoleklasseList.as_view(), name="class_list"),
    path("classes/create/", SkoleklasseCreate.as_view(), name="class_create"),
    path("classes/<int:pk>/update/", SkoleklasseUpdate.as_view(), name="class_update"),
    path("classes/<int:pk>/", SkoleklasseDetail.as_view(), name="class_detail"),
    # Teacher URLs
    path("teachers/", LærerList.as_view(), name="teacher_list"),
    path("teachers/create/", LærerCreate.as_view(), name="teacher_create"),
    path("teachers/<int:pk>/update/", LærerUpdate.as_view(), name="teacher_update"),
    # Exam URLs
    path("exams/", EksamenList.as_view(), name="exam_list"),
    path("exams/create/", EksamenCreate.as_view(), name="exam_create"),
    path("exams/<int:pk>/update/", EksamenUpdate.as_view(), name="exam_update"),
    path("exams/<int:pk>/", EksamenDetail.as_view(), name="exam_detail"),
    # Censor URLs
    path("censors/", CensorList.as_view(), name="censor_list"),
    path("censors/create/", CensorCreate.as_view(), name="censor_create"),
    path("censors/<int:pk>/update/", CensorUpdate.as_view(), name="censor_update"),
    path("censors/<int:pk>/", CensorDetail.as_view(), name="censor_detail"),
    # admin
    path("admin/", admin.site.urls),
    # test
    # Example: /2012/08/
    path(
        "<int:year>/<int:month>/",
        EksamenMonthArchive.as_view(month_format="%m"),
        name="archive_month_numeric",
    ),
    # Example: /2012/aug/
    path(
        "<int:year>/<str:month>/",
        EksamenMonthArchive.as_view(),
        name="archive_month",
    ),
]
