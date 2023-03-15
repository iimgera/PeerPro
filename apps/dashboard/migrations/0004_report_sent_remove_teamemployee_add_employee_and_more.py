# Generated by Django 4.1.7 on 2023-03-15 18:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0003_remove_report_week_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='sent',
            field=models.BooleanField(default=False, verbose_name='Отчет отправлен'),
        ),
        migrations.RemoveField(
            model_name='teamemployee',
            name='add_employee',
        ),
        migrations.AddField(
            model_name='teamemployee',
            name='add_employee',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Сотрудники команды'),
        ),
    ]
