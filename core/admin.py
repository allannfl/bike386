from django.contrib import admin

# Register your models here.
from .models import *
class FuncionarioAdmin(admin.ModelAdmin):
	list_display = ('nome', 'telefone', 'endereco', 'funcao', 'codigo')

class BicicletaAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'id', 'disponivel')

class EmpresaAdmin(admin.ModelAdmin):
	list_display= ('razaosocial','cnpj')

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('nome', 'telefone', 'endereco', 'codigo')

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'bicicleta', 'funcionario', 'data_criacao')

admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Bicicleta, BicicletaAdmin)
admin.site.register(Reserva, ReservaAdmin)