# Generated by Django 3.1.7 on 2022-03-24 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reg_jounals', '0003_logs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logs',
            name='doc_date',
        ),
        migrations.RemoveField(
            model_name='logs',
            name='number',
        ),
    ]
