import pytest
import uuid

from apps.associations.models import Associations

pytestmark = pytest.mark.django_db


class TestAssociationsModel:
    def test_associations_model(self, agent, lead):
        Associations.objects.create(agent=agent, lead=lead)
        assert uuid.UUID(str(Associations.objects.first().id), version=4)
