from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

from django.http import Http404

from .models import Politico
from .models import Partido


def index(request):

	template = loader.get_template('politico/index.html')

	return HttpResponse(template.render(None, request))

# Politicos ----------------------------------------------------------------------------------
def lista_politicos(request):

	politico_query_result = Politico.objects.order_by('-id')[:5]
	template = loader.get_template('politico/politicos.html')
	context = {
		'politico_query_result': politico_query_result,
	}

	# output = ', '.join([q.question_text for q in latest_question_list])
	return HttpResponse(template.render(context, request))
	# return HttpResponse("Hello, world. Polls index.")

def detalhes_politico(request, id_politico):
	# try:
	# 	question = Question.objects.get(pk=q_id)
	# except Question.DoesNotExist:
	# 	raise Http404("Question does not exist")

	politico = get_object_or_404(Politico, pk=id_politico)

	return render(request, 'politico/detalhes_politico.html', {'politico': politico})

# Partidos ----------------------------------------------------------------------------------
def lista_partidos(request):
	partidos_query_result = Politico.objects.order_by('-id')[:5]
	template = loader.get_template('politico/partidos.html')
	context = {
		'partidos_query_result': partidos_query_result,
	}

	# output = ', '.join([q.question_text for q in latest_question_list])
	return HttpResponse(template.render(context, request))
	# return HttpResponse("Hello, world. Polls index.")

def detalhes_partido(request, id_partido):
	# try:
	# 	question = Question.objects.get(pk=q_id)
	# except Question.DoesNotExist:
	# 	raise Http404("Question does not exist")

	partido = get_object_or_404(Partido, pk=id_partido)

	return render(request, 'politico/detalhes_partido.html', {'partido': partido})
