# Generated by Django 3.1.2 on 2023-02-16 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work_cal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workcalendarrecord',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]