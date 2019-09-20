from django.conf.urls import url

from ponto import views

urlpatterns = [

  url(r'^colaborador/(?P<id>[0-9]+)$', views.ColaboradorAPIView.as_view()),
  url(r'^colaborador/$', views.ColaboradorAPIListView.as_view()),

]


