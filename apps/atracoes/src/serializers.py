from rest_framework.serializers import ModelSerializer
from ..models import Atracao


class AtracaoSerializer(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ('id', 'nome', 'descricao', 'horario_funcionamento', 'idade_minima', 'foto')
