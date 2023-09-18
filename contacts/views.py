from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from common.pagination import Pagination
from contacts.models import Contact
from contacts.serializers import ContactFiltersSerializer, ContactSerializer


class ContactView(ModelViewSet):
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name']
    
    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)

    @extend_schema(parameters=[ContactFiltersSerializer])
    def list(self, request: Request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
