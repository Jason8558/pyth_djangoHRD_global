# Generated by Django 3.1.7 on 2021-04-26 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TURV', '0002_remove_tabelitem_shours38'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabelitem',
            name='sHours38',
            field=models.IntegerField(blank=True, null=True, verbose_name='Нерабочие оплачиваемые дни'),
        ),
    ]
