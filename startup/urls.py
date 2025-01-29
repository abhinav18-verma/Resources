from django.urls import path, include
from .views import ResourceListView, CreateStartupResources

urlpatterns = [
    path("", ResourceListView.as_view(), name="StartupResoureList"),
    path("create-data/", CreateStartupResources),
]
