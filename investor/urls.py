from django.urls import path, include
from .views import InvestorResourceList, CreateInvestorResources

urlpatterns = [
    path("", InvestorResourceList.as_view()),
    path("create-data/", CreateInvestorResources),
]
