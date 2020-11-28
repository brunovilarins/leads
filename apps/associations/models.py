from django.db import models
from uuid import uuid4


class Associations(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )

    agent = models.ForeignKey(
        to='agents.Agents',
        related_name='associations',
        on_delete=models.CASCADE,
        db_index=True,
    )

    lead = models.ForeignKey(
        to='leads.Leads',
        related_name='associations',
        on_delete=models.CASCADE,
        db_index=True,
        unique=True
    )

    associated_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'
        ordering = ['-associated_at']
