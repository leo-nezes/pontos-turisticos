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
    lookup_field = 'nome'

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
