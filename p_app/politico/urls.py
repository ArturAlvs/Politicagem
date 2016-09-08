from django.conf.urls import url

from . import views

app_name = 'politico'
urlpatterns = [
    # ex: /
    url(r'^$', views.index, name='index'),

	# ex: /politicos/ ----- Lista de politicos
    url(r'^politicos/$', views.lista_politicos, name='lista_politicos'),
    # ex: /politico/5/
    url(r'^politico/(?P<id_politico>[0-9]+)$', views.detalhes_politico, name='detalhes_politico'),

    # ex: /partidos/ -------- Lista de partidos
    url(r'^partidos/$', views.lista_partidos, name='lista_partidos'),
    # ex: /partido/5/ -------- Detalhes do partido
    url(r'^partido/(?P<id_partido>[0-9]+)$', views.detalhes_partido, name='detalhes_partido'),

    # ex: /politico/5/results/
    # url(r'^/#/(?P<id_partido>[0-9]+)/$', views.detalhes_partido, name='detalhes_partido'),


    # # ex: /polls/5/vote
    # url(r'^(?P<q_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
