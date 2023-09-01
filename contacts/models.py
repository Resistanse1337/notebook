from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import LifetimeModel
from users.models import User


class Contact(LifetimeModel):
    class Meta:
        verbose_name = _("Контакт")
        verbose_name_plural = _("Контакты")

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Владелец контакта"))

    first_name = models.CharField(max_length=64, verbose_name=_("Имя"))

    last_name = models.CharField(max_length=64, verbose_name=_("Фамилия"))

    phone_number = models.IntegerField(verbose_name=_("Номер телефона"))

    email = models.EmailField(verbose_name=_("Email"))
