# Generated by Django 3.1.2 on 2020-10-08 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reg_jounals', '0002_auto_20201009_1042'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='outbounddocument',
            options={'ordering': ['-doc_reg_date'], 'verbose_name': 'Исходящий документ', 'verbose_name_plural': 'Исходящие документы'},
        ),
        migrations.RemoveField(
            model_name='outbounddocument',
            name='doc_content',
        ),
    ]