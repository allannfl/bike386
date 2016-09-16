from django.db import models

# Create your models here.
class Funcionario(models.Model):
	nome = models.CharField(max_length=40)
	endereco = models.CharField(max_length=60)
	telefone = models.CharField(u'Celular', max_length=14, help_text='(99)99999-9999')
	codigo = models.CharField(max_length=10)
	funcao = models.CharField(max_length=40)
	email = models.EmailField

	def __str__(self):
		return self.nome


class Bicicleta(models.Model):
	marca = models.CharField(max_length=40)
	modelo = models.CharField(max_length=40)
	cor = models.CharField(max_length=20)
	descricao = models.CharField(max_length=100)
	situacao = models.CharField(max_length=2)


	def __str__(self):
		return self.marca


class Empresa(models.Model):
	razaosocial = models.CharField(max_length=40)
	cnpj=models.CharField(max_length=15)

	def __str__(self):
		return self.razaosocial


		
