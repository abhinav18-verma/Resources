from django.urls import path, include
from .views import CreateInvestorTools, InvestorToolsList

urlpatterns = [
    path("", InvestorToolsList.as_view()),
    path("create-data/", CreateInvestorTools),
]
