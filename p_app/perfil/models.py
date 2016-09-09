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

	# Foto do politico
	imagem = models.CharField(max_length=200, default="-")


	# Atributos de Politico ---------------------
	cargo_atual = models.ForeignKey(Cargo, on_delete=models.CASCADE, blank=True, null=True)
	# inicio_cargo = models.DateTimeField('Inicio do cargo atual')

	partido_atual = models.ForeignKey(Partido, on_delete=models.CASCADE, blank=True, null=True)

	# Colocar uma foreignKey pra uma busca mais rapida? Nao sei!
	# candidatura_atual = models.ForeignKey(Candidatura, on_delete=models.CASCADE, blank=True, null=True)


class Candidatura(models.Model):

	# Politico
	politico = models.ForeignKey(Politico, on_delete=models.CASCADE)

	eleito = models.BooleanField(default=True)

	id_eleitoral = models.IntegerField(default=0)


	inicio_periodo = models.DateTimeField('Inicio da Candidatura')
	final_periodo = models.DateTimeField('Final da Candidatura')

	# Poderia ser 2
	estado = models.CharField(max_length=20, default="-")

	# Total de doacao recebida na Candidatura
	total_doacao = models.IntegerField(default=0)


class Projeto(models.Model):
	titulo = models.CharField(max_length=200)

	inicio_andamento_projeto = models.DateTimeField('Inicio do andamento do projeto')

	andamento = models.CharField(max_length=200)
	data_andamento = models.DateTimeField('Data do andamento atual')

	criador = models.ForeignKey(Politico, on_delete=models.CASCADE)


class Doacao(models.Model):
	doador = models.CharField(max_length=200)
	valor  = models.IntegerField(default=0)

	politico = models.ForeignKey(Politico, on_delete=models.CASCADE)

class Bancada(models.Model):
	titulo = models.CharField(max_length=200)

class Colecao_Bancada(models.Model):
	bancada = models.ForeignKey(Bancada, on_delete=models.CASCADE, blank=True, null=True)
	politico = models.ForeignKey(Politico, on_delete=models.CASCADE)
