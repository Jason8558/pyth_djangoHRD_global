# Generated by Django 3.1.2 on 2021-02-01 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reg_jounals', '0030_auto_20210201_1641'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newordersonvacation',
            options={'ordering': ['id'], 'verbose_name': 'Приказ на отпуск', 'verbose_name_plural': 'Приказы на отпуск (новые)'},
        ),
    ]
