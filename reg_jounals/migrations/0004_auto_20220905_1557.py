# Generated by Django 3.1.7 on 2022-09-05 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_jounals', '0003_auto_20220905_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordersonpersonnel',
            name='op_dateOfInv',
            field=models.DateField(blank=True, db_index=True, default='NULL', help_text='Введите дату приема на работу', null=True, verbose_name='Дата приема на работу'),
        ),
    ]
