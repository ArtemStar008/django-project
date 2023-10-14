from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def read_post(request):
    return render(request, 'index.html')


def second_page(request):
    return render(request, 'second_page.html')


def third_page(request):
    return render(request, 'third_page.html')
