# Generated by Django 3.1.2 on 2020-10-08 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_jounals', '0003_auto_20201009_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='outbounddocument',
            name='doc_additionalData',
            field=models.CharField(blank=True, help_text='Введите дополнительную информацию по документу (необязательно)', max_length=256, verbose_name='Дополнительная информация'),
        ),
    ]
