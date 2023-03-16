from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone


class TeamEmployee(models.Model):
    name_team = models.CharField(max_length=70, verbose_name='Имя команды')
    description = models.TextField(verbose_name='Описание команды')

    def __str__(self):
        return self.name_team
    
    class Meta:
        verbose_name = 'Команда '
        verbose_name_plural = 'Команды'
        ordering = ['-id']



class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    week_start_date = models.DateField()
    last_week = models.TextField(
        blank=True, 
        verbose_name='What did you do last week?'
        )
    this_week = models.TextField(
        blank=True, 
        verbose_name='What are you working on until the next week?'
        )
    next_week = models.TextField(
        blank=True, 
        verbose_name='What are your plans for the next week?'
        )
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sent = models.BooleanField(default=False, verbose_name='Отчет отправлен')

    def save(self, *args, **kwargs):
        if not self.id:
            # Установка даты week_start_date при создании нового отчета
            self.week_start_date = timezone.now().date()
            # Установка даты deadline на неделю вперед от week_start_date
            self.deadline = self.week_start_date + timezone.timedelta(days=7)
        super(Report, self).save(*args, **kwargs)



    def __str__(self):
        return f"Report {self.id} by {self.user.username}"

    class Meta:
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'
        ordering = ['-id']



    
