from django.test import TestCase

from .models import ECBRate
from datetime import datetime
from pytz import timezone

# Create your tests here.

def tz():
    return timezone('Europe/Berlin')

class ECBRateTestCase(TestCase):
    def setUp(self):
        ECBRate.objects.create(date=datetime(2016,1,1,0,0,tzinfo=tz()), code="USD", rate="1.01")
        ECBRate.objects.create(date=datetime(2016,1,2,0,0,tzinfo=tz()), code="USD", rate="1.009")

    def test_rate_creation(self):
        """objects can be created and retrieved"""
        allusd = ECBRate.objects.all()
        self.assertEqual(2, len(allusd))

    def test_rate_search(self):
        """objects can be created and using key"""
        ARate = ECBRate.objects.get(rate="1.01")
        self.assertEqual(datetime(2016,1,1,0,0,tzinfo=tz()), ARate.date)

    # def test_rate_pri_key(self):
    #     """rate can be found by combination of date and code"""
