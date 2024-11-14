from django.db import models
from django.core.exceptions import ValidationError


class Category(models.Model):
    label = models.CharField(max_length=200, unique=True)
    value = models.CharField(max_length=50, blank=True, null=True)

    def save(self, *args, **kwargs):

        if not self.value:
            self.value = self.get_value_from_label(self.label)

        # Проверка уникальности label
        if Category.objects.filter(label=self.label).exclude(pk=self.pk).exists():
            raise ValidationError("Category with this label already exists.")

        super().save(*args, **kwargs)

    def get_value_from_label(self, label):

        translation = {
            'Автомобильные шины': 'car tires',
            'Грузовые шины': 'truck tires',
            'Мотошины': 'motorcycle tires',
            'аксессуары для шин, дисков и шиномонтажа': 'tire, rim, and tire service accessories',
            'Аккумуляторы': 'batteries',
            'Автомасла': 'motor oils',
            'Автоэлектроника': 'car electronics',
            'Автохимия и автокосметика': 'car chemicals and cosmetics',
            'внешний декор, тюнинг и защита': 'exterior decor, tuning, and protection',
            'Инструменты и техническая помощь': 'tools and technical assistance',
            'Компрессоры': 'compressors',
            'Услуги': 'services',
            'компания': 'company',
        }

        return translation.get(label, label.lower())

    def __str__(self):
        return self.label


class Tires(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    seasonality = models.CharField(max_length=255)
    width = models.FloatField()
    profile = models.CharField(max_length=255)
    diameter = models.CharField(max_length=255)
    speed_index = models.CharField(max_length=255)
    load_index = models.CharField(max_length=255)
    load_index_for_double = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=3, default=0, verbose_name='Цена')
    promotion = models.DecimalField(max_digits=10, decimal_places=3, default=0, verbose_name='Акция')
    quantity = models.IntegerField()

    def __str__(self):
        return self.title
