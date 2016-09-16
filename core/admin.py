from django.contrib import admin

# Register your models here.
from .models import Funcionario
from .models import Bicicleta
from .models import Empresa

class FuncionarioAdmin(admin.ModelAdmin):
	list_display = ('nome', 'telefone', 'endereco', 'funcao', 'codigo')

class BicicletaAdmin(admin.ModelAdmin):
	list_display = ('marca', 'modelo', 'cor', 'descricao', 'situacao')

class EmpresaAdmin(admin.ModelAdmin):
	list_display= ('razaosocial','cnpj')

admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Bicicleta, BicicletaAdmin)
admin.site.register(Empresa, EmpresaAdmin)
 