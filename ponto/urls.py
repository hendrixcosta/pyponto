from django.conf.urls import url

from django.urls import path


try:
  from django.conf.urls import patterns
except ImportError:
  pass
from ponto import views

from django.views.generic.base import TemplateView


urlpatterns = [

  url(r'^colaborador/(?P<id>[0-9]+)$', views.ColaboradorAPIView.as_view()),
  url(r'^colaborador/$', views.ColaboradorAPIListView.as_view()),

  url(r'^ponto/(?P<id>[0-9]+)$', views.PontoAPIView.as_view()),
  url(r'^ponto/$', views.PontoAPIListView.as_view()),

  url(r'^pontomes/$', views.PontoDetailAPIView.as_view()),

  path('vue/$', TemplateView.as_view(template_name='index.html')),

]
