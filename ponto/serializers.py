from rest_framework.serializers import ModelSerializer
from ponto.models import Colaborador


class ColaboradorSerializer(ModelSerializer):

    class Meta:
        model = Colaborador
        fields = '__all__'
