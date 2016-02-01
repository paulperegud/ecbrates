from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ECBRate(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, null=False)
    published = models.DateTimeField()
    code = models.CharField(max_length=3, null=False)
    rate = models.DecimalField(max_digits=30, decimal_places=4, null=False)

    def __unicode__():
        return self.code
