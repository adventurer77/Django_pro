from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def article_2023(request):
    return HttpResponse('<h1>Articles 2023</h1>')

def articles_by_year(request,year):
    return HttpResponse(f'<h1>Articles {year}</h1>')

def articles_by_year_month(request,year,month):
    return HttpResponse(f'<h1>Articles {year} - {month}</h1>')