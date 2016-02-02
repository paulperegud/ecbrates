from django.contrib import admin

# Register your models here.

from .models import ECBRate

class ECBRateAdmin(admin.ModelAdmin):
    list_display =["date", "code", "rate"]
    class Meta:
        model = ECBRate

admin.site.register(ECBRate, ECBRateAdmin)
