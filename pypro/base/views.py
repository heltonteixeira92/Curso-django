from django.http import HttpResponse
from django.shortcuts import render # noqa

# Create your views here.
# a view é responsável por responder as requisições que fazemos pelo navegador


def home(request):
    return HttpResponse('Olá Django')
