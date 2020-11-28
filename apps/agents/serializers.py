from rest_framework import serializers
from apps.agents.models import Agents


class AgentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agents
        fields = (
            'pk',
            'name',
            'seniority',
            'last_association',
            'score',
        )
