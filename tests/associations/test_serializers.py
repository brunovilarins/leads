import pytest
from apps.associations.serializers import AssociationSerializer

pytestmark = pytest.mark.django_db


class TestAssociationsModel:
    def test_associations_serializer_validate_success(self, associations_data):
        serializer = AssociationSerializer(data=associations_data)

        assert serializer.is_valid() is True

    def test_associations_serializer_not_valid(self, associations_data, agent_senior):
        serializer = AssociationSerializer(data=associations_data)

        assert serializer.is_valid() is False

    @pytest.mark.parametrize('field', ['agent', 'lead'])
    def test_associations_serializer_required_fields(self, field, associations_data):
        associations_data.pop(field)
        serializer = AssociationSerializer(data=associations_data)

        assert serializer.is_valid() is False
        error_message = str(serializer.errors[field][0])
        assert error_message == 'This field is required.'
