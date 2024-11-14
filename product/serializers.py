# serializers.py
from rest_framework import serializers
from .models import Tires, Category


class CategorySerializer(serializers.ModelSerializer):
    value = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['label', 'value']

    def get_value(self, obj):
        # Перевод значений label в value (на английском)
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

        # Используйте label для получения значения на английском
        return translation.get(obj.label, obj.label)

    def create(self, validated_data):
        label = validated_data.get('label')

        # Перевод на английский при создании
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

        # Устанавливаем value на английском
        validated_data['value'] = translation.get(label, label)

        return super().create(validated_data)


class TiresCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tires
        fields = '__all__'


from rest_framework import serializers
from .models import Tires

class TiresListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Tires
        fields = [
            'id',
            'title',
            'category',
            'seasonality',
            'price',
            'quantity',

        ]
