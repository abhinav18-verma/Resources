from django.urls import path, include
from .views import StartupResourceList, CreateStartupResources

urlpatterns = [
    path("", StartupResourceList.as_view(), name="StartupResoureList"),
    path("create-data/", CreateStartupResources),
]
