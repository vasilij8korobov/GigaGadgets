from django.db import models
from users.models import CustomUser
from contact.models import Contact
from product.models import Product


class NetworkNode(models.Model):
    """Модель звена торговой сети (Завод/Розничная сеть/ИП)"""

    # Уровни иерархии
    LEVEL_CHOICES = (
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'ИП')
    )
    name = models.CharField(max_length=100, verbose_name="Название звена")
    contacts = models.OneToOneField(Contact, on_delete=models.CASCADE, verbose_name="Контактные данные")
    products = models.ManyToManyField(Product, verbose_name="Продукты")
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Поставщик")
    debt_to_supplier = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Задолженность перед поставщиком (руб)")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    level = models.IntegerField(choices=LEVEL_CHOICES, editable=False, verbose_name="Уровень в иерархии")
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, verbose_name="Создатель записи")

    class Meta:
        verbose_name = "Звено сети"
        verbose_name_plural = "Звенья сети"
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.supplier:
            self.level = 0  # Завод
        else:
            self.level = self.supplier.level + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_level_display()}: {self.name}"

    def get_level_display(self):
        pass
