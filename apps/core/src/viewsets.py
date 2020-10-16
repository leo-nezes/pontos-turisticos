from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from ..models import PontoTuristico
from .serializers import PontoTuristicoSerializer


class PontoTuristicoViewSet(ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    filter_backends = (SearchFilter, )
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )
    search_fields = ('nome', 'descricao', 'endereco__linha1')
    lookup_field = 'id'

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)
        query_set = PontoTuristico.objects.all()

        if id:
            query_set = PontoTuristico.objects.filter(pk=id) # ou (id=id)

        if nome:
            query_set = query_set.filter(nome__iexact=nome)

        if descricao:
            query_set = query_set.filter(descricao__iexact=descricao)

        return query_set

    @action(methods=['post'], detail=True)
    def associa_atracoes(self, request, id):
        atracoes = request.data['ids']

        ponto = PontoTuristico.objects.get(id=id)

        ponto.atracoes.set(atracoes)

        ponto.save()

        return Response(status=status.HTTP_201_CREATED)
