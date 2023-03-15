# Generated by Django 4.1.7 on 2023-03-15 12:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_team', models.CharField(max_length=70, verbose_name='Имя команды')),
                ('description', models.TextField(verbose_name='Описание команды')),
                ('add_employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Команда ',
                'verbose_name_plural': 'Команды',
                'ordering': ['-id'],
            },
        ),
    ]