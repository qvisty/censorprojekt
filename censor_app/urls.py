# censor_app/urls.py
from django.urls import path
from . import views

app_name = 'censor_app'


urlpatterns = [
    path('censors/', views.CensorList.as_view(), name='censor_list'),
    path('censors/create/', views.CensorCreate.as_view(), name='censor_create'),
    path('censors/<int:pk>/update/', views.CensorUpdate.as_view(), name='censor_update'),
    path('classes/create/', views.ClassCreate.as_view(), name='class_create'),
    path('schools/<int:pk>/classes/', views.SchoolClassListView.as_view(), name='school_class_list'),
    path('', views.DashboardView.as_view(), name="dashboard"),
]


