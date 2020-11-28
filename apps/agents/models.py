from datetime import datetime
from django.db import models
from uuid import uuid4


class Agents(models.Model):

    SENIORITY = (
        (1, 1),
        (2, 1.5),
        (3, 2),
    )

    id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )

    name = models.CharField(
        max_length=100,
    )

    seniority = models.PositiveSmallIntegerField(choices=SENIORITY)

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )

    @property
    def score(self):
        association = self.associations.first()
        if association:
            last_association = datetime.strptime(
                association.associated_at.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S"
            )
            time_association = datetime.now() - last_association
            return int(time_association.total_seconds() / 3600) * self.get_seniority_display()
        else:
            return self.get_seniority_display()

    @property
    def last_association(self):
        association = self.associations.first()
        if association:
            return association.associated_at
        else:
            return None

    class Meta:
        verbose_name = 'Agent'
        verbose_name_plural = 'Agents'
