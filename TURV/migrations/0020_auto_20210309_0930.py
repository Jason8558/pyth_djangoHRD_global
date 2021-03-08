# Generated by Django 3.1.2 on 2021-03-08 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TURV', '0019_auto_20210302_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabel',
            name='ro_check',
            field=models.BooleanField(blank=True, default=False, verbose_name='Проверен РО'),
        ),
        migrations.AddField(
            model_name='tabelitem',
            name='sHours36',
            field=models.IntegerField(blank=True, null=True, verbose_name='Местная командировка'),
        ),
    ]
