import pytest
from rest_framework import status
from rest_framework.reverse import reverse

pytestmark = pytest.mark.django_db


class TestAssociationsModel:
    def test_post_success(self, api_client, agent, lead):
        url = reverse('associations:associations-list')
        association_data = {
            'agent': agent.pk,
            'lead': lead.pk
        }
        response = api_client.post(url, association_data)

        assert response.status_code == status.HTTP_201_CREATED
        assert bool(response.data) is True

    def test_post_with_score_pre_conditions(self, api_client, agent, agent_senior, lead):
        url = reverse('associations:associations-list')
        association_data = {
            'agent': agent.pk,
            'lead': lead.pk
        }
        response = api_client.post(url, association_data)

        assert response.status_code == status.HTTP_412_PRECONDITION_FAILED


