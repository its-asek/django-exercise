from django.urls import path
from . import views

app_name = "pesel_decoder"
urlpatterns = [
    path("", views.home, name="home"),
]
