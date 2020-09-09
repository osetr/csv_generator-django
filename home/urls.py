from django.urls import path
from .views import HomeView, delete_schema_ajax

urlpatterns = [
    path(r"", HomeView.as_view(), name="home_v"),
    path(
        r"ajax/delete_schema/<pk>",
        delete_schema_ajax,
        name="delete_schema_ajax_v"
    ),
]
