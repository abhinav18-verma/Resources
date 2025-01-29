from django.urls import path, include
from .views import InvestorResourceListView, CreateInvestorResources

urlpatterns = [
    path("", InvestorResourceListView.as_view(), name="StartupResoureList"),
    path("create-data/", CreateInvestorResources),
]
