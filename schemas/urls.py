from django.urls import path, include
from .views import *

urlpatterns = [
    path("new/", AddSchemaView.as_view(), name="add_schema_v"),
    path("edit/<pk>", EditSchemaView.as_view(), name="edit_schema_v"),
    path(
        r"ajax/generate_data/<pk>/<int:rows>",
        generate_data_ajax,
        name="generate_data_ajax_v",
    ),
    path(
        r"ajax/check_celery_job/<pk>/", chech_celery_job_ajax, name="check_celery_job_v"
    ),
    path("media/<file_id>/", download_file),
]
