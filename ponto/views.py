from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from ponto.serializers import ColaboradorSerializer, PontoSerializer
from ponto.models import Colaborador, Ponto


class PontoDetailAPIView(APIView):

    def get(self, request, *args, **kwargs):
        """
        """
        id_colaborador = request.query_params.get('id')
        mes = request.query_params.get('mes')

        if id_colaborador:
            colaborador_id = Colaborador.objects.get(pk=id_colaborador)

            if mes:
                reg_ponto_ids = colaborador_id.getPontoMesColaborador(mes)

        return Response(data={
            'detailsPontoMes':reg_ponto_ids,
        })

    def post(self, request, *args, **kwargs):
        my_result = 'Hendrix'
        return Response(data={"my_return_data":my_result})



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
