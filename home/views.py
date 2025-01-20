# Create your views here.
from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("A view index funcionou, Wow!")

def sobre(request):
    return HttpResponse("<h1>Sistema 1.0 desenvolvido por mim<h1>")

def contato(request):
    return HttpResponse("Esssa é a página de contato")

def ajuda(request):
    return HttpResponse("Essa é a pagina de ajuda")

def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato (request):
    return render(request, 'contato.html')

def ajuda (request):
    return render (request, 'ajuda.html')
