# Generated by Django 4.1.1 on 2022-12-05 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TURV', '0014_alter_employers_aup'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShiftShedModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=4, verbose_name='Год')),
                ('checked', models.BooleanField(default=0, verbose_name='Проверен')),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TURV.department', verbose_name='Подразделение')),
            ],
            options={
                'verbose_name': 'График сменности',
                'verbose_name_plural': 'Графики сменности',
            },
        ),
    ]