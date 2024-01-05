import json
from uuid import uuid4
from django.db import models

from django.db.models import (
    CharField, TextField, DateTimeField
)



class Entry(models.Model):
    class EntryTypes(models.TextChoices):
        REQUEST = "REQUEST"

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    type = CharField(max_length=20, choices=EntryTypes)
    content = TextField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    @property
    def uuid(self):
        return str(self.id)
