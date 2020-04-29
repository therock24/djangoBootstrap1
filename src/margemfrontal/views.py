from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})

def oportunidades(request):
    return render(request, 'oportunidades.html', {})