# Generated by Django 3.1.2 on 2020-12-23 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_jounals', '0007_auto_20201224_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordersonvacation',
            name='oov_number',
            field=models.CharField(blank=True, db_index=True, help_text='Введите номер приказа', max_length=10, verbose_name='Номер приказа'),
        ),
    ]
