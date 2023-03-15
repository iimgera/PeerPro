from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from datetime import date
from apps.dashboard.models import Report



class ReportExcelViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_report_excel_view(self):
        url = reverse('report-excel')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.get('Content-Disposition'), 
            'attachment; filename="report.xlsx"'
        )
        self.assertEqual(response['Content-Type'], 'application/vnd.ms-excel')