from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length = 128)
    email = models.EmailField('E-mail', null = True, blank = True)

    def __str__(self):
        return self.nome

class Compromisso(models.Model):
    nome = models.CharField('Título', max_length = 64)
    data = models.DateField('Dia marcado')
    hora = models.TimeField('Hora')

    def __str__(self):
        return self.nome

class Agenda(models.Model):
    criador = models.ForeignKey(Pessoa, on_delete = models.CASCADE, default = None)
    nome = models.CharField('Nome', max_length = 128)
    visibilidade = models.BooleanField(default = False, verbose_name='Tornar privado?')
    compromisso = models.ManyToManyField(Compromisso)

    def __str__(self):
        return self.nome

class AgendaInstitucional(models.Model):
    nome = models.CharField('Nome', max_length = 128)
    compromisso = models.ManyToManyField(Compromisso)

    def __str__(self):
        return self.nome
