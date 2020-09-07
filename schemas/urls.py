from django.urls import path, include
from .views import *

urlpatterns = [
    path("new_schema/", AddSchemaView.as_view(), name="add_schema_v"),
]
