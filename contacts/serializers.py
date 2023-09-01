from rest_framework import serializers

from contacts.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "created_at",
        ]

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class ContactFiltersSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
