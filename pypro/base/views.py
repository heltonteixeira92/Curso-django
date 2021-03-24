from django.shortcuts import render

# Create your views here.
# a view é responsável por responder as requisições que fazemos pelo navegador


def home(request):
    return render(request, 'base/home.html')
