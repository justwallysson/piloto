# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("A view index funcionou, Wow!")

def sobre(request):
    return HttpResponse("<h1>Sistema 1.0 desenvolvido por mim<h1>")

def contato(request):
    return HttpResponse("Esssa é a página de contato")

def ajuda(request):
    return HttpResponse("Essa é a pagina de ajuda")