from django.urls import path, include
from .views import InvestorResourceList, CreateInvestorResources

urlpatterns = [
    path("", InvestorResourceList),
    path("create-data/", CreateInvestorResources),
]
