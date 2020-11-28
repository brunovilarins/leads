from rest_framework import serializers
from apps.agents.models import Agents
from apps.associations.models import Associations


class AssociationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Associations
        fields = (
            'pk',
            'agent',
            'lead',
            'associated_at',
        )

    def validate(self, data):
        print('validando')
        agents = sorted(Agents.objects.all(), key=lambda m: m.score, reverse=True)
        if agents:
            if agents[0].pk != data.get('agent').pk and agents[0].score != data.get('agent').score:
                raise serializers.ValidationError(
                    {'errors': f'Association not is valid ! Next Agent is {agents[0].pk}'}
                )

        return data
