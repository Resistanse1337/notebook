from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet

from common.pagination import Pagination
from contacts.models import Contact
from contacts.serializers import ContactFiltersSerializer, ContactSerializer


class ContactView(ModelViewSet):
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = Pagination
    
    def get_queryset(self):
        query = Contact.objects.filter(user=self.request.user)

        if first_name := self.request.query_params.get("first_name"):
            query = query.filter(first_name__icontains=first_name)
        
        if last_name := self.request.query_params.get("last_name"):
            query = query.filter(last_name__icontains=last_name)

        return query

    @extend_schema(parameters=[ContactFiltersSerializer])
    def list(self, request: Request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
