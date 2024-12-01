# Generated by Django 5.1.3 on 2024-12-01 14:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_status', models.CharField(choices=[('Free', 'Свободен'), ('Reserved', 'Забронирован')], max_length=255, verbose_name='Статус бронирования стола')),
                ('reservation_date', models.DateField(verbose_name='Забронированная дата')),
                ('reservation_start', models.TimeField(verbose_name='Забронированное время')),
                ('reservation_duration', models.TimeField(verbose_name='Продолжительность бронирования')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания бронирования')),
                ('reservation_number', models.CharField(blank=True, max_length=6, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Бронь',
                'verbose_name_plural': 'Брони',
            },
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.PositiveIntegerField(unique=True, verbose_name='Номер стола')),
                ('table_size', models.CharField(choices=[('Small', 'На 1-2 персон'), ('Big', 'На 3+ персон')], max_length=255, verbose_name='Размер стола')),
                ('table_status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking.reservation')),
            ],
            options={
                'verbose_name': 'Стол',
                'verbose_name_plural': 'Столы',
            },
        ),
    ]
