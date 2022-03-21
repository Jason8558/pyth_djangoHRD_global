# Generated by Django 3.1.7 on 2022-01-13 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TURV', '0003_tabel_unloaded'),
    ]

    operations = [
        migrations.CreateModel(
            name='Overtime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField(db_index=True, verbose_name='Период')),
                ('value_m', models.FloatField(default=0, verbose_name='Значение_мужчины')),
                ('value_w', models.FloatField(default=0, verbose_name='Значение_женщины')),
            ],
            options={
                'verbose_name': 'Норма времени',
                'verbose_name_plural': 'Нормы врмени',
                'ordering': ['-year'],
            },
        ),
        migrations.AddField(
            model_name='employers',
            name='sex',
            field=models.CharField(choices=[('М', 'М'), ('Ж', 'Ж')], db_index=True, default='М', max_length=1, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='tabel',
            name='year',
            field=models.CharField(db_index=True, max_length=4, verbose_name='Год'),
        ),
        migrations.AlterField(
            model_name='tabelitem',
            name='bound_tabel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TURV.tabel', verbose_name='Св. табель'),
        ),
        migrations.AlterField(
            model_name='tabelitem',
            name='sHours1',
            field=models.FloatField(blank=True, help_text='Явки', null=True, verbose_name='Явки (Я)'),
        ),
        migrations.AlterField(
            model_name='tabelitem',
            name='v_hours',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Часов неявок'),
        ),
        migrations.AlterField(
            model_name='tabelitem',
            name='w_hours',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Часов отработано'),
        ),
    ]
