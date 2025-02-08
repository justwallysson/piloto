# Create your views here.
from django.shortcuts import render, HttpResponse



LISTA_ALUNOS = [
    {"nome": "João Silva", "matricula": "202301", "curso": "Técnico em Informática", "data_nascimento": "20/01/2008" , "turma": "208"},
    {"nome": "Maria Oliveira", "matricula": "202302", "curso": "Técnico em Informática", "data_nascimento": "20/01/2008", "turma": "208"},
    {"nome": "Carlos Souza", "matricula": "202303", "curso": "Técnico em Informática", "data_nascimento": "20/01/2008" , "turma": "208"},
]
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

def local (request):
    return render (request, 'local.html')

def exibiritem(request,id):
    return render(request,'exibiritem.html',{'id':id})

def dados(request):
    context = {
        'nome': 'João',
        'idade': 16,
        'cidade': 'Teresina'
    }
    return render(request,'dados.html',context)

def form(request):
    if request.method == "POST": 
        # captura cada informação digitada no formulário
        nome = request.POST.get("nome")
        idade = request.POST.get("idade")
        cidade = request.POST.get("cidade")
        # cria um dicionário context com os dados capturados
        context = {
            'nome': nome,
            'idade': idade,
            'cidade': cidade
        }
        # mostra os dados capturados no template dados.html
        return render(request,'dados.html',context)
    else: # method GET, mostra o formulário vazio
        return render(request,'form.html')

def listar_alunos(request):
    context = {
        'lista': LISTA_ALUNOS,
    }
    return render(request, 'listar_alunos.html', context)


from django.shortcuts import redirect

def editar_aluno(request, indice):
    aluno = LISTA_ALUNOS[indice]  # Obtém a referência do aluno na lista


    if request.method == "POST":
        # Atualiza diretamente os valores do dicionário aluno
        aluno['nome'] = request.POST.get("nome")
        aluno['matricula'] = request.POST.get("matricula")
        aluno['curso'] = request.POST.get("curso")
        aluno['data_de_nascimento'] = request.POST.get("data_de_nascimento")
        aluno['turma'] = request.POST.get("turma")


        return redirect('listar_alunos')  # Redireciona para a lista de alunos


    context = {
        'aluno': aluno,
        'indice': indice
    }
    return render(request, 'form_aluno.html', context)
