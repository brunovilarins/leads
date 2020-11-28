import pytest
from rest_framework import status
from rest_framework.reverse import reverse

pytestmark = pytest.mark.django_db


class TestAgentsModel:
    def test_list(self, api_client, agent):
        url = reverse('agents:agents-list')
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert bool(response.data) is True

    @pytest.mark.parametrize('seniority', [1, 2, 3])
    def test_post(self, seniority, api_client):
        url = reverse('agents:agents-list')
        agent_data = {
            'name': 'string',
            'seniority': seniority
        }
        response = api_client.post(url, agent_data)

        assert response.status_code == status.HTTP_201_CREATED
        assert bool(response.data) is True

    @pytest.mark.parametrize('seniority', [11, 12, 13])
    def test_post_with_bad_request(self, seniority, api_client, ):
        url = reverse('agents:agents-list')
        agent_data = {
            'name': 'string',
            'seniority': seniority
        }
        response = api_client.post(url, agent_data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
