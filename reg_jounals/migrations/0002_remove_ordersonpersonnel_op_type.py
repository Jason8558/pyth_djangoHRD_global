# Generated by Django 3.1.7 on 2022-03-18 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reg_jounals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordersonpersonnel',
            name='op_type',
        ),
    ]
