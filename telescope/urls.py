from django.urls import path

from . import views

urlpatterns = [
    path("requests", views.index, name="index"),
]
