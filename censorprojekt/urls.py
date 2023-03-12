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
    # skole URLs
    path("skole/<int:pk>/update/", SkoleUpdate.as_view(), name="skole_update"),
    path("skole/create/", SkoleCreate.as_view(), name="skole_create"),
    path("skole/<int:pk>/", SkoleDetail.as_view(), name="skole_detail"),
    path("skoler/", SkoleList.as_view(), name="skole_list"),
    # skoleklasse URLs
    path("skoleklasser/", SkoleklasseList.as_view(), name="skoleklasse_list"),
    path("skoleklasse/create/", SkoleklasseCreate.as_view(), name="skoleklasse_create"),
    path(
        "skoleklasse/<int:pk>/update/",
        SkoleklasseUpdate.as_view(),
        name="skoleklasse_update",
    ),
    path(
        "skoleklasse/<int:pk>/", SkoleklasseDetail.as_view(), name="skoleklasse_detail"
    ),
    # Teacher URLs
    path("lærere/", LærerList.as_view(), name="lærer_list"),
    path("lærer/create/", LærerCreate.as_view(), name="lærer_create"),
    path("lærer/<int:pk>/update/", LærerUpdate.as_view(), name="lærer_update"),
    path("lærer/<int:pk>/", LærerDetail.as_view(), name="lærer_detail"),
    # Exam URLs
    path("eksamen/", EksamenList.as_view(), name="eksamen_list"),
    path("eksamen/create/", EksamenCreate.as_view(), name="eksamen_create"),
    path("eksamen/<int:pk>/update/", EksamenUpdate.as_view(), name="eksamen_update"),
    path("eksamen/<int:pk>/", EksamenDetail.as_view(), name="eksamen_detail"),
    # Censor URLs
    path("censor/", CensorList.as_view(), name="censor_list"),
    path("censor/create/", CensorCreate.as_view(), name="censor_create"),
    path("censor/<int:pk>/update/", CensorUpdate.as_view(), name="censor_update"),
    path("censor/<int:pk>/", CensorDetail.as_view(), name="censor_detail"),
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
    # admin
    path("admin/", admin.site.urls, name="admin"),
]
