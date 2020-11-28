from apps.associations.models import Associations
from apps.associations.serializers import AssociationSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response


class AssociationViewSet(ModelViewSet):
    queryset = Associations.objects.all()
    serializer_class = AssociationSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_412_PRECONDITION_FAILED)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
