from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from datetime import date
from apps.dashboard.models import Report

