from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ECBRate(models.Model):
    class Meta:
        unique_together = (('date','target'),)
    timestamp = models.DateTimeField(auto_now_add=True, null=False)
    date = models.DateTimeField("publication date, as defined by ECB")
    base = models.CharField("base currency code", max_length=3, default="EUR")
    target = models.CharField("target currency code", max_length=3, null=False)
    rate = models.DecimalField("exchange rate", max_digits=30, decimal_places=4, null=False)

    @classmethod
    def create(arate, date, base, target, rate):
        return arate(date = date, base = base, target = target, rate = rate)

    def __unicode__(self):
        return str(self.date) + self.target
