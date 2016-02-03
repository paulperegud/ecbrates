from django.test import TestCase

from .models import ECBRate
from .parser import fetch_and_parse

from datetime import datetime
from pytz import timezone
import os
import subprocess

# Create your tests here.

def tz():
    return timezone('Europe/Berlin')

class ECBRateTestCase(TestCase):
    def setUp(self):
        ECBRate.objects.create(date=datetime(2016,1,1,0,0,tzinfo=tz()), code="USD", rate="1.01")
        ECBRate.objects.create(date=datetime(2016,1,1,0,0,tzinfo=tz()), code="PLN", rate="4.30")
        ECBRate.objects.create(date=datetime(2016,1,2,0,0,tzinfo=tz()), code="USD", rate="1.009")

    def test_rate_creation(self):
        """objects can be created and retrieved"""
        allusd = ECBRate.objects.all()
        self.assertEqual(3, len(allusd))

    def test_rate_search(self):
        """objects can be found using rate"""
        ARate = ECBRate.objects.get(rate="1.01")
        self.assertEqual(datetime(2016,1,1,0,0,tzinfo=tz()), ARate.date)

    def test_uniqueness(self):
        """two datapoints for same date/rate can't be created"""
        try:
            ECBRate.objects.create(date=datetime(2016,1,1,0,0,tzinfo=tz()), code="USD", rate="1.01")
            self.fail("uniqueness constraint failed")
        except:
            pass

class ParserTestCase(TestCase):
    def test_population(self):
        fn = os.path.join(subprocess.check_output('pwd')[:-1], 'ecbrates/priv/fxref-usd.xml')
        R = fetch_and_parse('file://'+fn)
        self.assertEqual(5, len(R))
