from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("<h1>Nitra smrdí</h1>")
    # return render(request, "home.html")
