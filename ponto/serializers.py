from rest_framework.serializers import ModelSerializer
from ponto.models import Colaborador, Ponto


class ColaboradorSerializer(ModelSerializer):

    class Meta:
        model = Colaborador
        fields = '__all__'


class PontoSerializer(ModelSerializer):

    class Meta:
        model = Ponto
        fields = '__all__'
