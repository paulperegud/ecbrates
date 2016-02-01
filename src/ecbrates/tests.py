from django.test import TestCase

from .models import ECBRate
from datetime import datetime
from pytz import timezone

# Create your tests here.

class ECBRateTestCase(TestCase):
    def setUp(self):
        Warsaw =timezone('Europe/Warsaw')
        ECBRate.objects.create(date=datetime(2016,1,1,0,0,tzinfo=Warsaw), code="USD", rate="1.01")
        ECBRate.objects.create(date=datetime(2016,1,2,0,0,tzinfo=Warsaw), code="USD", rate="1.009")

    def test_rate_creation(self):
        """objects can be created and retrieved"""
        allusd = ECBRate.objects.all()
        self.assertEqual(2, len(allusd))

    def test_rate_search(self):
        """objects can be created and using key"""
        Warsaw =timezone('Europe/Warsaw')
        ARate = ECBRate.objects.get(rate="1.01")
        self.assertEqual(datetime(2016,1,1,0,0,tzinfo=Warsaw), ARate.date)
