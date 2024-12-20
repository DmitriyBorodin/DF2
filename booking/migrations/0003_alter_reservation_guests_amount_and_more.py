# Generated by Django 5.1.3 on 2024-12-03 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_remove_reservation_reservation_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='guests_amount',
            field=models.CharField(default='1-2', verbose_name='Количество гостей'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reservation_date',
            field=models.DateField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reservation_start',
            field=models.TimeField(verbose_name='Время'),
        ),
    ]
