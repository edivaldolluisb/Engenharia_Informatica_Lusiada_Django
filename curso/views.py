from django.shortcuts import render
from .models import Ano, Disciplina, AgendaTeste, AgendaEntrega, Calendario

# Create your views here.


def index(request):
    return render(request, 'curso/index.html')


def anos(request):
    disciplinas = Disciplina.objects.all()
    return render(request, 'curso/anos.html', {
        'disciplinas': disciplinas,
    })


def ver_disciplina(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    return render(request, 'curso/disciplina.html', {
        'disciplina': disciplina
    })


def calendario(request):
    calendarios = Calendario.objects.all()
    return render(request, 'curso/calendario.html', {
        'calendario': calendarios
    })


def agenda(request):
    testes = AgendaTeste.objects.all()
    entregas = AgendaEntrega.objects.all()
    return render(request, 'curso/agenda.html', {
        'testes': testes,
        'entregas': entregas,
    })
