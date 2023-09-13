from django.db import transaction
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from common.models import LifetimeModel
from .tasks import send_mail


class User(AbstractUser, LifetimeModel):
    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")

    def __str__(self) -> str:
        return f"User #{self.id} {self.username}"
    
    @staticmethod
    def create_user(validated_data: dict) -> "User":
        with transaction.atomic():
            user = User.objects.create(
                first_name=validated_data["first_name"],
                last_name=validated_data["last_name"],
                username=validated_data["username"],
                email=validated_data["email"],
            )

            user.set_password(validated_data["password"])
            user.save()

            return user
        
    def send_mail(self, subject: str, email_html_message: str) -> None:
        send_mail.delay(self.email, subject, email_html_message)
