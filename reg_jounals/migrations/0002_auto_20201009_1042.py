# Generated by Django 3.1.2 on 2020-10-08 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reg_jounals', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='outbounddocument',
            options={'ordering': ['doc_reg_date'], 'verbose_name': 'Исходящий документ', 'verbose_name_plural': 'Исходящие документы'},
        ),
    ]