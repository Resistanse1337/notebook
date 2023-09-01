from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "first_name", "last_name", "username", "created_at",)
    list_display_links = ("id",)
    ordering = ("pk",)
