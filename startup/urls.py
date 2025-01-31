from django.urls import path, include
from .views import StartupResourceList, CreateStartupResources

urlpatterns = [
    path("", StartupResourceList, name="StartupResoureList"),
    path("create-data/", CreateStartupResources),
]
