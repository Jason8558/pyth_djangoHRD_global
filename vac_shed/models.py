from django.db import models
from TURV.models import Employers as TEmps
from TURV.models import Department as TDeps


class VacantionShedule(models.Model):
    dep = models.ForeignKey('TURV.Department', verbose_name="Подразделение", on_delete=models.CASCADE)
    year = models.IntegerField(verbose_name="Период", db_index=True)
    sup_check = models.BooleanField(verbose_name='Утвержден СУП', default=False)
    res_officer = models.CharField(verbose_name="Ответственный", max_length=256, default='')
    class Meta:
        ordering = ['-year']
        verbose_name = 'График отпусков'
        verbose_name_plural = 'Графики отпусков'

    def __str__(self):
        name = 'График отпусков ' + self.dep.name + ' за ' + str(self.year) + ' год'
        return name

class VacantionSheduleItem(models.Model):
    bound_shed = models.ForeignKey('VacantionShedule', on_delete=models.CASCADE)
    emp = models.ForeignKey('TURV.Employers', on_delete = models.CASCADE, verbose_name="Сотрудник")
    reason = models.ForeignKey('VacantionReasons', null=True, blank=True, on_delete=models.CASCADE, verbose_name='Причина отсутствия')
    dur_from = models.DateField(verbose_name="Период с")
    dur_to = models.DateField(verbose_name="Период по")
    move_from = models.DateField(verbose_name='Перенос с: ', null=True, blank=True)
    move_to = models.DateField(verbose_name='перенос по: ', null=True, blank=True)
    move_reason = models.TextField(help_text="Введите основание переноса", verbose_name="Основание переноса", default='')
    child_year = models.CharField(verbose_name='Год рож-я иждивенца: ', null=True, blank=True, max_length=4, default='')
    city = models.CharField(verbose_name='Проезд: ', null=True, blank=True, max_length=254, default='')
    days_count = models.IntegerField(verbose_name="Количество дней")
    days_count_move = models.IntegerField(verbose_name='Кол-во дней после переноса ', null=True, blank=True)
    comm = models.CharField(verbose_name='Комментарий', null=True, blank=True, max_length=256)

    class Meta:
        ordering = ['-bound_shed__year']
        verbose_name = 'Элемент графика'
        verbose_name_plural = 'Элементы графика'
    def __str__(self):
        name = self.emp.fullname + ' ' +str(self.bound_shed.year)
        return name
    
class VacantionReasons(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=100, null=False, blank=False)

    class Meta:
        ordering = ['name']
        verbose_name = 'Причина отсутствия'
        verbose_name_plura = 'Причины отсутствия'
    def __str__(self):
        return self.name

# Create your models here.
