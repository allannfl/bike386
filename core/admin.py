from django.contrib import admin

# Register your models here.
from .models import Funcionario
from .models import Bicicleta
from core.models import Cliente
from core.models import Empresa


class FuncionarioAdmin(admin.ModelAdmin):
	list_display = ('nome', 'telefone', 'endereco', 'funcao', 'codigo')

class BicicletaAdmin(admin.ModelAdmin):
	list_display = ('marca', 'modelo', 'cor', 'descricao', 'situacao')


class ClienteAdmin(admin.ModelAdmin):
	list_display = ('nome', 'cpf', 'registro', 'endereco', 'telefone', 'debito', 'statos')

class EmpresaAdmin(admin.ModelAdmin):
	list_display = ('nome','cnpj','codigo', 'endereco', 'telefone')



admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Bicicleta, BicicletaAdmin)

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Empresa, EmpresaAdmin)
