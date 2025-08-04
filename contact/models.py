from django.db import models
from users.models import CustomUser


class Contact(models.Model):
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=100, verbose_name="страна")
    city = models.CharField(max_length=100, verbose_name="город")
    street = models.CharField(max_length=100, verbose_name="улица")
    house_number = models.CharField(max_length=20, verbose_name="номер дома")
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Контакты ({self.city}, {self.street})"
