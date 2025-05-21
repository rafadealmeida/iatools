from django.shortcuts import render
from django.http import HttpResponse
from galeria.models import IATool

def index(request):
    categoria = request.GET.get('categoria')
    
    ias = IATool.objects.filter(publicada=True)
   
    if categoria:
        ias = ias.filter(categoria=categoria)

    categorias = IATool.OPCOES_CATEGORIA

    return render(request, 'galeria/index.html', {
        'cards': ias,
        'categorias': categorias,
        'categoria_ativa': categoria
    })

def imagem(request,id):
    try:
        ia = IATool.objects.get(id=id)
    except IATool.DoesNotExist:
        return HttpResponse("Imagem não encontrada", status=404)
    
    return render(request, 'galeria/imagem.html',{"card":ia})


def buscar(request):
    try:
        query = request.GET.get('search') 
        resultados = IATool.objects.filter(nome__icontains=query) if query else []
    except IATool.DoesNotExist:
        return HttpResponse("Imagem não encontrada", status=404)

    return render(request, 'galeria/buscar.html', {'resultados': resultados, 'query': query})

def contato(request):
    return render(request, 'galeria/contato.html')
