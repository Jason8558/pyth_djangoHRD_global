# Generated by Django 3.1.2 on 2021-06-30 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TURV', '0002_employers_fired'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabel',
            name='unloaded',
            field=models.BooleanField(blank=True, default=False, verbose_name='Загружен в 1С'),
        ),
    ]