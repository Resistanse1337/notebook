from django.contrib import admin

from contacts.models import Contact



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "phone_number", "email", "created_at",)
    list_display_links = ("id",)
    ordering = ("pk",)