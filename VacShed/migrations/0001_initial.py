# Generated by Django 3.1.7 on 2022-04-14 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TURV', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VacantionShedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(db_index=True, verbose_name='Период')),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TURV.department', verbose_name='Подразделение')),
            ],
            options={
                'verbose_name': 'График отпусков',
                'verbose_name_plural': 'Графики отпусков',
                'ordering': ['-year'],
            },
        ),
    ]
