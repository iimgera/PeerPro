from django.contrib import admin

from apps.dashboard.models import Report, TeamEmployee

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = (
            'id', 
            'user', 
            'last_week', 
            'this_week', 
            'next_week',
            'deadline', 
            'created_at', 
            'updated_at'
        )
    list_filter = (
        'created_at', 
        'updated_at'
        )
    
admin.site.register(TeamEmployee)  
