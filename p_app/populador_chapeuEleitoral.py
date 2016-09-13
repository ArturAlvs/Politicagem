# import django
# django.setup()

# --------------

# from .models import Cargos
#
# Cargos.objects.all()


from perfil.models import *
from datetime import *

import json
from pprint import pprint
import codecs
from django.utils import timezone


# data = json.loads(open('populadores/0.json').read().decode('utf-8-sig') )

with open('populadores/0.json') as data_file:
    data = json.load(data_file)

# pprint("Printing data")
# pprint(data)
# pprint("Data printed")

d = Politico.objects.all()
pprint(d)

politico_nomeCompleto = data['fullname']
# Usar partition ou split?
politico_nome = politico_nomeCompleto.partition(' ')[0]
politico_sobrenome = politico_nomeCompleto[len(politico_nome)+1:]

politico_imagem = data['image']

# Essas duas linhas funcionam pq os dados sao da eleicao de 2014 (escrito em 11/Set/2016)
politico_cargo = data['title']
candidatura_partido = data['party']

try:
    cargoObj = Cargo.objects.get(titulo=politico_cargo)
except Exception as e:
    cargoObj = Cargo(titulo=politico_cargo, salario=0)
    cargoObj.save()

try:
    partidoObj = Partido.objects.get(nome=candidatura_partido)
except Exception as e:
    partidoObj = Partido(nome=candidatura_partido)
    partidoObj.save()

# Procurar se politico ja existe
try:
    politicoObj = Politico.objects.get(nome=politico_nome, sobrenome=politico_sobrenome)
except Politico.DoesNotExist:
    # politicoObj = Politico(nome=politico_nome, sobrenome=politico_sobrenome, imagem=politico_imagem)
    politicoObj = partidoObj.politico_set.create(nome=politico_nome, sobrenome=politico_sobrenome, imagem=politico_imagem, cargo_atual=cargoObj)
    # politicoObj.save()
    # colecao_bancadasObj = politicoObj.colecao_bancada_set.create()

candidatura_como_foi_eleito = data['status']
candidatura_estado = data['state']
candidatura_total_doacao = data['total']
candidatura_id_eleitoral = data['election_id']

# Colocar as datas
candidatura_inicio = datetime(2014, 1, 1)
candidatura_fim = datetime(2018, 12, 31)


# Juntando Plotico e Candidatura
candidaturaObj = politicoObj.candidatura_set.create(eleito=True, como_foi_eleito=candidatura_como_foi_eleito, id_eleitoral=candidatura_id_eleitoral, inicio_periodo=candidatura_inicio, final_periodo=candidatura_fim, estado=candidatura_estado, total_doacao=candidatura_total_doacao, partido=partidoObj)

# TO-DO doacoes___________
candidatura_doacoes = data['donations']
for doacao in candidatura_doacoes:
    candidaturaObj.doacao_set.create(doador=doacao, valor=candidatura_doacoes[doacao])
    # print(doacao)
    # print(candidatura_doacoes[doacao])

# TO-DO bancadas___________
# candidatura_bancadas = data['stands']
# for bancada in candidatura_bancadas:
#     print(bancada)




# print(politico_nomeCompleto.partition(' ')[0])



# a = 'ca\xc3'
# pprint(a)
# a.decode('UTF-8')
# print(a)
