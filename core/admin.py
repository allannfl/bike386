from django.contrib import admin

# Register your models here.
from .models import Funcionario
from .models import Bicicleta

class FuncionarioAdmin(admin.ModelAdmin):
	list_display = ('nome', 'telefone', 'endereco', 'funcao', 'codigo')

class BicicletaAdmin(admin.ModelAdmin):
	list_display = ('marca', 'modelo', 'cor', 'descricao', 'situacao')


admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Bicicleta, BicicletaAdmin)
