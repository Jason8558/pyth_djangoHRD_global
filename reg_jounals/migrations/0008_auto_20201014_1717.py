# Generated by Django 3.1.2 on 2020-10-14 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_jounals', '0007_auto_20201013_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outbounddocument',
            name='doc_res_officer',
            field=models.CharField(blank=True, default='none', help_text='Сотрудник, который внес документ в систему ', max_length=256, verbose_name='Ответственный сотрудник'),
        ),
    ]
