# Generated by Django 3.0.5 on 2020-09-09 11:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Schema",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
                ("separator", models.CharField(max_length=10)),
                (
                    "date",
                    models.DateTimeField(
                        default=datetime.datetime(2020, 9, 9, 11, 42, 23, 792652),
                        editable=False,
                    ),
                ),
                ("columns", djongo.models.fields.JSONField()),
                (
                    "author",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Processing",
            fields=[
                (
                    "file_id",
                    models.UUIDField(
                        default=uuid.UUID("c164f93f-1436-47cd-a326-7a6e2b3c93dc"),
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "date",
                    models.DateTimeField(
                        default=datetime.datetime(2020, 9, 9, 11, 42, 23, 793143),
                        editable=False,
                    ),
                ),
                ("file_ready", models.BooleanField(default=False)),
                ("rows", models.IntegerField()),
                (
                    "schema",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="schemas.Schema",
                    ),
                ),
            ],
        ),
    ]
