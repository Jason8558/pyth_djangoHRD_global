# Generated by Django 3.1.7 on 2021-06-03 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TURV', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employers',
            name='fired',
            field=models.BooleanField(default=False, verbose_name='Сотрудник уволен'),
        ),
    ]
