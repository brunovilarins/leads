from apps.leads.models import Leads
from apps.leads.serializers import LeadsSerializer

from rest_framework.viewsets import ModelViewSet


class LeadsViewSet(ModelViewSet):
    queryset = Leads.objects.all()
    serializer_class = LeadsSerializer
    http_method_names = ['post']
