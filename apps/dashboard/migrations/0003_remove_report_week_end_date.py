# Generated by Django 4.1.7 on 2023-03-15 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_teamemployee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='week_end_date',
        ),
    ]
