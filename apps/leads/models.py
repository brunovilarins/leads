from django.db import models
from uuid import uuid4


class Leads(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )

    name = models.CharField(
        max_length=100,
    )

    phone_number = models.CharField(
        max_length=11,
    )

    class Meta:
        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'
