#-*- enconding: utf-8 -*-
from django import forms

class PessoaForm(forms.Form):
	nome = forms.CharField(max_length=100)
	idade = forms.InteregerField(max_length=3)
	data_nascimento = forms.DateTimeFiels()
	endereco = forms.CharField(max_length=150)
	cidade = forms.CharField(max_length=50)
	telefone = forms.CharField(max_length=13, required=True)
	email = forms.EmailField(max_length=100)
	celular = forms.CharField(max_length=13, required=True)
	cpf = forms.CharField(max_length=14)
	rg = forms.CharField(max_length=10)
