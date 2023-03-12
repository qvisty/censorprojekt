# censor_app/urls.py
from django.urls import path
from . import views

app_name = "censor_app"


urlpatterns = [
    # home
    path("", views.Dashboard.as_view(), name="dashboard"),

]
