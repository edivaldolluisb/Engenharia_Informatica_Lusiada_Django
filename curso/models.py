from django.db import models
from django.utils import timezone

# Create your models here.


class Disciplina(models.Model):
    nome = models.CharField(max_length=50)
    nome_curto = models.CharField(max_length=10, blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.nome


class Ano(models.Model):
    ano = models.CharField(max_length=5)
    ano_nome = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.ano


class Sala(models.Model):
    nome = models.CharField(max_length=10)

    def __str__(self):
        return self.nome


class AgendaTeste(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.DO_NOTHING)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.DO_NOTHING)
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.sala.nome


class AgendaEntrega(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.DO_NOTHING)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.DO_NOTHING)
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.sala.nome


class Calendario(models.Model):
    nome = models.CharField(max_length=20, default='calendario')
    foto = models.ImageField(upload_to='calendario/%Y%m')
    foto2 = models.ImageField(upload_to='calendario/%Y%m', blank=True, null=True)

    def __str__(self):
        return self.nome
