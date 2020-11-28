import pytest
from apps.agents.serializers import AgentsSerializer


class TestAgentsModel:
    def test_agent_serializer_validate_success(self, agent_data):
        serializer = AgentsSerializer(data=agent_data)

        assert serializer.is_valid() is True

    @pytest.mark.parametrize('field', ['name', 'seniority'])
    def test_agent_serializer_required_fields(self, field, agent_data):
        agent_data.pop(field)
        serializer = AgentsSerializer(data=agent_data)

        assert serializer.is_valid() is False
        error_message = str(serializer.errors[field][0])
        assert error_message == 'This field is required.'
