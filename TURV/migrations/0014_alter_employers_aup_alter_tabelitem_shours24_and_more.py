# Generated by Django 4.1.1 on 2022-12-13 02:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TURV', '0013_alter_department_dir_alter_department_union'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employers',
            name='aup',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dep_aup', to='TURV.department', verbose_name='Подчиненное подразделение'),
        ),
        migrations.AlterField(
            model_name='tabelitem',
            name='sHours24',
            field=models.FloatField(blank=True, null=True, verbose_name='Выходные (В)'),
        ),
        migrations.AlterField(
            model_name='tabelitem',
            name='sHours3',
            field=models.FloatField(blank=True, null=True, verbose_name='Работа в выходные и празд. (РВ)'),
        ),
    ]
