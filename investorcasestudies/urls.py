from django.urls import path, include
from .views import CreateInvestorCaseStudies, InvestorCaseStudiesList

urlpatterns = [
    path("", InvestorCaseStudiesList.as_view()),
    path("create-data/", CreateInvestorCaseStudies),
]
