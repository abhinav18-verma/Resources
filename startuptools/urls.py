from django.urls import path, include
from .views import CreateStartupTools, StartupToolsList

urlpatterns = [
    path("", StartupToolsList.as_view()),
    path("create-data/", CreateStartupTools),
]
