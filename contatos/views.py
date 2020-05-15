from django.shortcuts import render
from .models import Contato


def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html', {
        'contatos':contatos
    })


def showContato(request, contatoId):
    contato = Contato
    return render(request, 'contatos/showContato.html', {
        'contato':contato
    })

