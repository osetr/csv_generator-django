from django.urls import path, include
from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name="home_v"),
    path(r"ajax/delete_schema/<pk>", delete_schema_ajax, name="delete_schema_ajax_v"),
]
