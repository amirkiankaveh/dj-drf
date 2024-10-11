import uuid
from django.db import models


class Media(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    dir = models.CharField(max_length=100, default="/beton/")
    url = models.URLField()
