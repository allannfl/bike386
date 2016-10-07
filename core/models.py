from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class Funcionario(models.Model):
	usuario = models.ForeignKey('auth.User') 
	nome = models.CharField(max_length=40)
	endereco = models.CharField(max_length=60)
	telefone = models.CharField(max_length=13)
	codigo = models.IntegerField()
	funcao = models.CharField(max_length=40)
	email = models.EmailField
	


	def __str__(self):
		return self.nome

class Bicicleta(models.Model):
    modelo_bicicleta = (
        ('BMX', 'BMX'),
        ('FRONTIER','FRONTIER WIN'),
        ('FOX','FOX'),
        ('ONIX', 'ONIX VB')
    )

    modelo = models.CharField(max_length=30,
                              choices=modelo_bicicleta)

    disponivel = models.BooleanField()


    def __str__(self):
        return self.modelo + ' - Código ' + str(self.id)


class Cliente(models.Model):
    nome = models.CharField(max_length = 100)
    cpf = models.CharField(max_length = 11)
    registro = models.CharField(max_length = 30)
    endereco = models.CharField(max_length = 40)
    telefone = models.CharField(max_length = 20)
    debito = models.CharField(max_length = 30)
    status = models.CharField(max_length = 30)

    def __str__(self):
        return self.nome

class Reserva(models.Model):
    bicicleta = models.ForeignKey('Bicicleta')
    cliente = models.ForeignKey(Cliente)
    funcionario = models.ForeignKey(Funcionario)
    data_criacao = models.DateTimeField(auto_created=True)
    data_retirada = models.DateTimeField(auto_created=True)
    data_devolucao = models.DateTimeField(default=None, null=True, blank=True)

    def __str__(self):
        return self.cliente.nome

class Empresa(models.Model):
    nome = models.CharField(max_length = 100)
    cnpj = models.CharField(max_length = 20)
    codigo = models.CharField(max_length = 30)
    endereco = models.CharField(max_length = 40)
    telefone = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.nome
