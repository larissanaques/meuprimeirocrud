#-*- enconding: utf-8 -*-
from django.db import models

class PessoaModel (models.Model):
	nome = models.CharField(max_length=100)
	idade = models.IntegerField(max_length=3)
	data_nascimento = models.DateTimeField()
	endereco = models.CharField(max_length=150)
	cidade = models.CharField(max_length=50)
	telefone = models.CharField(max_length=13, null=True)
	email = models.EmailField(max_length=100)
	celular = models.CharField(max_length=13, null=True)
	cpf = models.CharField(max_length=14)
	rg = models.CharField(max_length=10)



	
		