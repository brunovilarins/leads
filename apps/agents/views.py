from apps.agents.models import Agents
from apps.agents.serializers import AgentsSerializer

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class AgentsViewSet(ModelViewSet):
    queryset = Agents.objects.all()
    serializer_class = AgentsSerializer
    http_method_names = ['get', 'post']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(
            sorted(queryset, key=lambda m: m.score, reverse=True), many=True
        )
        return Response(serializer.data)
