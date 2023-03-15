# Generated by Django 4.1.7 on 2023-03-15 23:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teamemployee',
            options={'ordering': ['-id'], 'verbose_name': 'Team', 'verbose_name_plural': 'Teams'},
        ),
        migrations.AlterField(
            model_name='report',
            name='sent',
            field=models.BooleanField(default=False, verbose_name='Report sent'),
        ),
        migrations.AlterField(
            model_name='teamemployee',
            name='add_employee',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Team members'),
        ),
        migrations.AlterField(
            model_name='teamemployee',
            name='description',
            field=models.TextField(verbose_name='Description of the team'),
        ),
        migrations.AlterField(
            model_name='teamemployee',
            name='name_team',
            field=models.CharField(max_length=70, verbose_name='Team name'),
        ),
    ]
