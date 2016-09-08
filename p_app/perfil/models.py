from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Cargo(models.Model):
	titulo = models.CharField(max_length=200)

	salario = models.IntegerField(default=0)

class Partido(models.Model):
	nome = models.CharField(max_length=200)


class Politico(models.Model):

	# Atributos de Pessoa -------
	nome = models.CharField(max_length=20)
	sobre_nome = models.CharField(max_length=100)
	idade = models.IntegerField(default=0)


	# Atributos de Politico ---------------------
	cargo_atual = models.ForeignKey(Cargo, on_delete=models.CASCADE, blank=True, null=True)
	# inicio_cargo = models.DateTimeField('Inicio do cargo atual')

	partido_atual = models.ForeignKey(Partido, on_delete=models.CASCADE, blank=True, null=True)


class Candidatura(models.Model):

	# Politico
	politico = models.ForeignKey(Politico, on_delete=models.CASCADE)

	eleito = models.BooleanField(default=True)

	inicio_periodo = models.DateTimeField('Inicio da Candidatura')
	final_periodo = models.DateTimeField('Final da Candidatura')


class Projeto(models.Model):
	titulo = models.CharField(max_length=200)

	inicio_andamento_projeto = models.DateTimeField('Inicio do andamento do projeto')

	andamento = models.CharField(max_length=200)
	data_andamento = models.DateTimeField('Data do andamento atual')

	criador = models.ForeignKey(Politico, on_delete=models.CASCADE)
