from django.contrib import admin
from .models import Pessoa, Agenda, Compromisso, AgendaInstitucional

# Register your models here.

@admin.register(Pessoa, Agenda, Compromisso, AgendaInstitucional)
class PessoaAdmin(admin.ModelAdmin):
	pass

class AgendaAdmin(admin.ModelAdmin):
	pass

class CompromissoAdmin(admin.ModelAdmin):
	pass

class AgendaInstitucionalAdmin(admin.ModelAdmin):
	pass