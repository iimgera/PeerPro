from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from dashboard.models import Report
from dashboard.serializers import ReportSerializer



class ReportList(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = (IsAuthenticated, IsAdminUser )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = (IsAuthenticated, IsAdminUser )
