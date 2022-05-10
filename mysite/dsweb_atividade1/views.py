from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    html = "<html><body>Italo Gabriel da Silva Monteiro, Matricula: 20211014040019</body></html>"
    return HttpResponse(html)
