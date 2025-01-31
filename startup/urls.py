from django.urls import path, include
from .views import ResourceListView, CreateStartupResources, add_data, fetch_paginated_data

urlpatterns = [
    path("", ResourceListView.as_view(), name="StartupResoureList"),
    path("create-data/", CreateStartupResources),
    path("person/", add_data),
    path("people/", fetch_paginated_data)
]
