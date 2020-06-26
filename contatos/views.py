from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Contato


def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html', {
        'contatos':contatos
    })


def showContato(request, idContato):
    contato = get_object_or_404(Contato, id=idContato)
    return render(request, 'contatos/showContato.html', {
        'contato':contato
    })


