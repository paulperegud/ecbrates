from django.shortcuts import render

from .models import ECBRate
from .worker import background_parsing

def listrates(request):
    all = ECBRate.objects.all()
    context = {
        "rates": all,
        "emptydb": len(all) < 1,
    }
    return render(request, "list.html", context)

def updaterates(request):
    feeds = [
        'https://www.ecb.europa.eu/rss/fxref-usd.html',
        'https://www.ecb.europa.eu/rss/fxref-pln.html',
        'https://www.ecb.europa.eu/rss/fxref-jpy.html',
    ]
    background_parsing(feeds)
    return render(request, "loading.html", {})
