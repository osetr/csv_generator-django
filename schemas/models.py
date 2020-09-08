from djongo import models
from accounts.models import User
from datetime import datetime
from django.utils import timezone


class Schema(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=64)
    separator = models.CharField(max_length=10)
    date = models.DateTimeField(default=timezone.now(), editable=False)
    columns = models.JSONField()
