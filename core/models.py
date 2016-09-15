from django.db import models

# Create your models here.
class Funcionario(models.Model):
	nome = models.CharField(max_length=40)
	endereco = models.CharField(max_length=60)
	telefone = models.CharField(max_length=15)
	codigo = models.CharField(max_length=10)
	funcao = models.CharField(max_length=40)


	def __str__(self):
		return self.nome


class Bicicleta(models.Model):
	marca = models.CharField(max_length=40)
	modelo = models.CharField(max_length=40)
	cor = models.CharField(max_length=20)
	descricao = models.CharField(max_length=100)
	situacao = models.CharField(max_length=2)


	def __str__(self):
		return self.modelo

class Cliente(models.Model):
    nome = models.CharField(max_length = 100)
    cpf = models.CharField(max_length = 11)
    registro = models.CharField(max_length = 30)
    endereco = models.CharField(max_length = 40)
    telefone = models.CharField(max_length = 20)
    debito = models.CharField(max_length = 30)
    statos = models.CharField(max_length = 30)

    def __str__(self):
        return self.nome

class Empresa(models.Model):
    nome = models.CharField(max_length = 100)
    cnpj = models.CharField(max_length = 20)
    codigo = models.CharField(max_length = 30)
    endereco = models.CharField(max_length = 40)
    telefone = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.nome
