from rest_framework import serializers
from dashboard.models import Report

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = (
            'id', 
            'user', 
            'last_week', 
            'this_week', 
            'next_week',
            'deadline', 
            'created_at', 
            'updated_at'
            )
            
        read_only_fields = (
            'id', 
            'user', 
            'deadline', 
            'created_at', 
            'updated_at')