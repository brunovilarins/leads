from rest_framework import serializers
from apps.leads.models import Leads


class LeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = (
            'pk',
            'name',
            'phone_number',
        )
