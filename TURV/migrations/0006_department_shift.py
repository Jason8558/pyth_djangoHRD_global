# Generated by Django 4.1.1 on 2022-10-30 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TURV', '0005_employers_aup'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='shift',
            field=models.BooleanField(default=False, verbose_name='Подразделение содержит сменщиков'),
        ),
    ]
