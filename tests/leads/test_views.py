import pytest
from rest_framework import status
from rest_framework.reverse import reverse

pytestmark = pytest.mark.django_db


class TestLeadsModel:
    def test_lead_post(self, api_client):
        url = reverse('leads:leads-list')
        lead_data = {
            'name': 'Fulano',
            'phone_number': '11236584564'
        }
        response = api_client.post(url, lead_data)

        assert response.status_code == status.HTTP_201_CREATED
        assert bool(response.data) is True

    @pytest.mark.parametrize('field', ['name', 'phone_number'])
    def test_post_with_bad_request(self, field, api_client, ):
        url = reverse('leads:leads-list')
        lead_data = {
            'name': 'string',
            'phone_number': '1123654484'
        }
        lead_data.pop(field)
        response = api_client.post(url, lead_data)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
