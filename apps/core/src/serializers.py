from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from ..models import PontoTuristico
from apps.atracoes.src.serializers import AtracaoSerializer
from apps.enderecos.src.serializers import EnderecoSerializer


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto', 'atracoes', 'comentarios',
                  'avaliacoes', 'endereco', 'descricao_completa', 'descricao_completa2')

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)
