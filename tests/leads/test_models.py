import pytest
import uuid

from apps.leads.models import Leads

pytestmark = pytest.mark.django_db


class TestLeadsModel:
    def test_leads_model(self):
        Leads.objects.create(name="Fulano", phone_number='11236594567')
        assert uuid.UUID(str(Leads.objects.first().id), version=4)
