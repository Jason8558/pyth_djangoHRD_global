# Generated by Django 4.1.1 on 2022-10-13 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TURV', '0002_employers_mainworkplace'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employers',
            name='mainworkplace',
            field=models.BooleanField(blank=True, default=True, verbose_name='Основная специальность'),
        ),
    ]
