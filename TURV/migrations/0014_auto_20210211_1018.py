# Generated by Django 3.1.2 on 2021-02-10 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TURV', '0013_auto_20210208_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tabelitem',
            name='department',
        ),
        migrations.RemoveField(
            model_name='tabelitem',
            name='level',
        ),
        migrations.RemoveField(
            model_name='tabelitem',
            name='position',
        ),
        migrations.RemoveField(
            model_name='tabelitem',
            name='positionOfPayment',
        ),
    ]