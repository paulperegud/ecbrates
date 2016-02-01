from django.shortcuts import render

# Create your views here.

def listrates(request):
    return render(request, "list.html", {})

def updaterates(request):
    return render(request, "loading.html", {})
