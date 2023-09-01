from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from common.models import LifetimeModel


class User(AbstractUser, LifetimeModel):
    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")

    def __str__(self) -> str:
        return f"User #{self.id} {self.username}"
