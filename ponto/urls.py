from django.conf.urls import url
try:
  from django.conf.urls import patterns
except ImportError:
  pass
from ponto import views

urlpatterns = [

  url(r'^colaborador/(?P<id>[0-9]+)$', views.ColaboradorAPIView.as_view()),
  url(r'^colaborador/$', views.ColaboradorAPIListView.as_view()),

  url(r'^ponto/(?P<id>[0-9]+)$', views.PontoAPIView.as_view()),
  url(r'^ponto/$', views.PontoAPIListView.as_view()),

  url(r'^pontomes/$', views.PontoDetailAPIView.as_view()),

]
