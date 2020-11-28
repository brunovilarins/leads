import pytest
from apps.leads.serializers import LeadsSerializer


class TestLeadsModel:
    def test_serializer_validate_success(self, lead_data):
        serializer = LeadsSerializer(data=lead_data)

        assert serializer.is_valid() is True

    @pytest.mark.parametrize('field', ['name', 'phone_number'])
    def test_serializer_required_fields(self, field, lead_data):
        lead_data.pop(field)
        serializer = LeadsSerializer(data=lead_data)

        assert serializer.is_valid() is False
        error_message = str(serializer.errors[field][0])
        assert error_message == 'This field is required.'
