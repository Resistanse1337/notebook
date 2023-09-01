from django.urls import path

from . import views

urlpatterns = [
    path("api/contacts/", views.ContactView.as_view({"get": "list", "post": "create"})),
    path("api/contacts/<int:pk>/", views.ContactView.as_view({"get": "retrieve", "delete": "destroy", "patch": "partial_update"})),
]