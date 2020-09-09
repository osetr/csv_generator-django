from djongo import models
from accounts.models import User
from datetime import datetime
import uuid


# model to storage all info for schema
# backend saves columns in following format
# {
#     'name': column name, 
#     'type': column type, 
#     'order': order in full columns list, 
#     'additional_parametrs': dict of addparams if they are required
# }
class Schema(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=64)
    separator = models.CharField(max_length=10)
    date = models.DateTimeField(default=datetime.now(), editable=False)
    columns = models.JSONField()

    def __str__(self):
        return "%s by %s" % (self.name, self.author)


# storage all required data to create new csv file
# file_ready serves to note if job is done or not
# and all in all it include file_id, that helps to
# find file in media dir
class Processing(models.Model):
    file_id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField(default=datetime.now(), editable=False)
    file_ready = models.BooleanField(default=False)
    rows = models.IntegerField()

    def __str__(self):
        return "schema %s with %s rows" % (self.schema.id, self.rows)
