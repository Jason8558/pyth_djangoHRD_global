# Generated by Django 4.1.1 on 2022-12-26 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorkCalendarRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4, verbose_name='Год')),
                ('month', models.IntegerField(verbose_name='Месяц')),
                ('days', models.CharField(max_length=256, verbose_name='Дни')),
            ],
            options={
                'verbose_name': 'Запись в календаре',
                'verbose_name_plural': 'Производственный календарь',
            },
        ),
    ]
