# Generated by Django 5.1.3 on 2024-12-03 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_alter_reservation_guests_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='reservation_commentary',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Пожелания к брони'),
        ),
    ]
