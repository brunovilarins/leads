import pytest
import uuid

from apps.agents.models import Agents
from apps.associations.models import Associations
from apps.leads.models import Leads

from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture()
def agent_data():
    return {'name': 'Agent', 'seniority': 1}


@pytest.fixture()
def agent():
    return Agents.objects.create(name='Agent', seniority=1)


@pytest.fixture()
def agent_senior():
    return Agents.objects.create(name='Agent', seniority=3)


@pytest.fixture()
def lead_data():
    return {'name': 'Fulano', 'phone_number': '1112314564'}


@pytest.fixture()
def lead():
    return Leads.objects.create(name='Fulano', phone_number='1112314564')


@pytest.fixture()
def associations_data(agent, lead):
    return {'agent': agent.pk, 'lead': lead.pk}


# @pytest.fixture()
# def associations():
#     return Associations.objects.create(name='Agent', seniority=1)
