from django.urls import path, include
from .views import CreateStartupCaseStudies, StartupCaseStudiesList

urlpatterns = [
    path("", StartupCaseStudiesList.as_view()),
    path("create-data/", CreateStartupCaseStudies),
]
