import pytest
import uuid

from apps.agents.models import Agents

pytestmark = pytest.mark.django_db


class TestAgentsModel:
    def test_agents_model(self):
        Agents.objects.create(name="Agent", seniority=2)
        assert uuid.UUID(str(Agents.objects.first().id), version=4)
