from rest_framework import serializers
from apps.dashboard.models import Report, TeamEmployee, ReportTeam

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = (
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


class TeamEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamEmployee
        fields = (
            'id',
            'name_team',
            'description'
        )


     