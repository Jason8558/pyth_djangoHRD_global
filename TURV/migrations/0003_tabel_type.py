# Generated by Django 3.1.7 on 2022-04-06 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TURV', '0002_remove_tabel_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='tabel',
            name='type',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='TURV.tabeltype', verbose_name='Вид '),
        ),
    ]
