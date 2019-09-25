from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from ponto.serializers import ColaboradorSerializer, PontoSerializer
from ponto.models import Colaborador, Ponto


class PontoDetailAPIView(APIView):


    def getDetailsColaborar_idMes(self, id_colaborador, mes):
        """
        """

        if not id_colaborador or not mes:
            return Response(status=500)

        if not Colaborador.objects.filter(id__exact=id_colaborador):
            return {'ERRO': 'Colaborador não cadastrado!'}

        colaborador_id = Colaborador.objects.get(pk=id_colaborador)
        detailsPontoMes = colaborador_id.getPontoMesColaborador(mes)
        return detailsPontoMes

    def get(self, request, *args, **kwargs):
        """
        """
        id_colaborador = request.query_params.get('id')
        mes = request.query_params.get('mes')

        detailsPontoMes = self.getDetailsColaborar_idMes(id_colaborador, mes)

        return Response(data={
            'detailsPontoMes': detailsPontoMes,
        })

    def post(self, request, format=None):
        """
        """

        id_colaborador = request.data.get('colaborador_id')
        mes = request.data.get('mes')

        detailsPontoMes = self.getDetailsColaborar_idMes(id_colaborador, mes)

        return Response(data={
            'detailsPontoMes': detailsPontoMes,
        })


class ColaboradorAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Colaborador.objects.get(pk=id)
            serializer = ColaboradorSerializer(item)
            return Response(serializer.data)
        except Colaborador.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Colaborador.objects.get(pk=id)
        except Colaborador.DoesNotExist:
            return Response(status=404)
        serializer = ColaboradorSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Colaborador.objects.get(pk=id)
        except Colaborador.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ColaboradorAPIListView(APIView):

    def get(self, request, format=None):
        items = Colaborador.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = ColaboradorSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ColaboradorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class PontoAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Ponto.objects.get(pk=id)
            serializer = PontoSerializer(item)
            return Response(serializer.data)
        except Ponto.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Ponto.objects.get(pk=id)
        except Ponto.DoesNotExist:
            return Response(status=404)
        serializer = PontoSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Ponto.objects.get(pk=id)
        except Ponto.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class PontoAPIListView(APIView):

    def get(self, request, format=None):
        items = Ponto.objects.all()
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = PontoSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = PontoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
