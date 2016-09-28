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

class Empresa(models.Model):
	razaosocial = models.CharField(max_length=40)
	cnpj=models.CharField(max_length=15)

	def __str__(self):
		return self.razaosocial

class Cliente(models.Model):
	usuario = models.ForeignKey('auth.User') 
	nome = models.CharField(max_length=40)
	endereco = models.CharField(max_length=60)
	telefone = models.CharField( max_length=14, help_text='(99)99999-9999')
	codigo = models.IntegerField()
	email = models.EmailField()

	def __str__(self):
		return self.nome
		
class Reserva(models.Model):
    bicicleta = models.ForeignKey(Bicicleta)
    cliente = models.ForeignKey(Cliente)
    funcionario = models.ForeignKey(Funcionario)
    data_criacao = models.DateTimeField(auto_created=True)
    data_retirada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cliente.nome