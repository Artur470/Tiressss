# Generated by Django 5.1.2 on 2024-10-22 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tires',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('width', models.FloatField()),
                ('load_index_for_double', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=3, default=0, max_digits=10, verbose_name='Цена')),
                ('promotion', models.DecimalField(decimal_places=3, default=0, max_digits=10, verbose_name='акция')),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
