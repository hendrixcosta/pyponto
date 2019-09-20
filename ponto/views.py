from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from ponto.serializers import ColaboradorSerializer, PontoSerializer
from ponto.models import Colaborador, Ponto


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
