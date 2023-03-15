from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.dashboard.models import TeamEmployee, Report


@admin.register(TeamEmployee)
class UserAdmin(admin.ModelAdmin):
    list_display = ( 
            'id',
            'name_team',
            'description'
            )

@admin.register(Report)
class UserAdmin(admin.ModelAdmin):
    list_display = (
            'id', 
            'user', 
            'week_start_date',
            'last_week', 
            'this_week', 
            'next_week',
            'deadline', 
            'created_at', 
            'updated_at',
            'sent',
            )