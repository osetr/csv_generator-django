from djongo import models


class Column(models.Model):
    info = models.JSONField()

    class Meta:
        abstract = True

class Schema(models.Model):
    name = models.CharField(max_length=64)
    separator = models.CharField(max_length=10)
    columns = models.JSONField()


