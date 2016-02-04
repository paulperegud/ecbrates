from django.shortcuts import render

from .models import ECBRate
from django.db import IntegrityError
# Create your views here.

def listrates(request):
    all = ECBRate.objects.all()
    context = {
        "rates": all,
        "emptydb": len(all) < 1,
    }
    return render(request, "list.html", context)

def updaterates(request):
    from .parser import fetch_and_parse
    rates = fetch_and_parse('https://www.ecb.europa.eu/rss/fxref-usd.html')
    for i in rates:
        try:
            i.save()
        except IntegrityError:
            pass
    return render(request, "loading.html", {})
