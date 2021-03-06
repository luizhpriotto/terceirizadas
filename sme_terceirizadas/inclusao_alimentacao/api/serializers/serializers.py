from rest_framework import serializers

from ....cardapio.api.serializers.serializers import (
    CombosVinculoTipoAlimentoSimplesSerializer,
    CombosVinculoTipoAlimentoSimplissimaSerializer
)
from ....dados_comuns.api.serializers import LogSolicitacoesUsuarioSerializer
from ....escola.api.serializers import (
    EscolaSimplesSerializer,
    FaixaEtariaSerializer,
    PeriodoEscolarSerializer,
    PeriodoEscolarSimplesSerializer
)
from ....inclusao_alimentacao.models import (
    GrupoInclusaoAlimentacaoNormal,
    InclusaoAlimentacaoContinua,
    InclusaoAlimentacaoDaCEI,
    InclusaoAlimentacaoNormal,
    MotivoInclusaoContinua,
    MotivoInclusaoNormal,
    QuantidadeDeAlunosPorFaixaEtariaDaInclusaoDeAlimentacaoDaCEI,
    QuantidadePorPeriodo
)


class MotivoInclusaoContinuaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotivoInclusaoContinua
        exclude = ('id',)


class MotivoInclusaoNormalSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotivoInclusaoNormal
        exclude = ('id',)


class QuantidadeDeAlunosPorFaixaEtariaDaInclusaoDeAlimentacaoDaCEISerializer(serializers.ModelSerializer):
    faixa_etaria = FaixaEtariaSerializer()

    class Meta:
        model = QuantidadeDeAlunosPorFaixaEtariaDaInclusaoDeAlimentacaoDaCEI
        exclude = ('id', 'inclusao_alimentacao_da_cei')


class InclusaoAlimentacaoDaCEISerializer(serializers.ModelSerializer):
    escola = EscolaSimplesSerializer()
    prioridade = serializers.CharField()
    periodo_escolar = PeriodoEscolarSimplesSerializer()
    tipos_alimentacao = CombosVinculoTipoAlimentoSimplissimaSerializer(many=True, read_only=True)
    motivo = MotivoInclusaoNormalSerializer()
    quantidade_alunos_por_faixas_etarias = QuantidadeDeAlunosPorFaixaEtariaDaInclusaoDeAlimentacaoDaCEISerializer(
        many=True, read_only=True)
    logs = LogSolicitacoesUsuarioSerializer(many=True)
    id_externo = serializers.CharField()
    escola = EscolaSimplesSerializer()

    def to_representation(self, instance):
        retorno = super().to_representation(instance)

        # Inclui o total de alunos nas faixas et??rias num per??odo
        qtde_alunos = instance.escola.alunos_por_periodo_e_faixa_etaria(
            instance.data
        )
        nome_periodo = 'INTEGRAL' if instance.periodo_escolar.nome == 'PARCIAL' else instance.periodo_escolar.nome
        for faixa_etaria in retorno['quantidade_alunos_por_faixas_etarias']:
            uuid_faixa_etaria = faixa_etaria['faixa_etaria']['uuid']
            faixa_etaria['total_alunos_no_periodo'] = qtde_alunos[nome_periodo][uuid_faixa_etaria]

        return retorno

    class Meta:
        model = InclusaoAlimentacaoDaCEI
        exclude = ('id',)


class QuantidadePorPeriodoSerializer(serializers.ModelSerializer):
    periodo_escolar = PeriodoEscolarSerializer()
    tipos_alimentacao = CombosVinculoTipoAlimentoSimplesSerializer(many=True, read_only=True)

    class Meta:
        model = QuantidadePorPeriodo
        exclude = ('id',)


class InclusaoAlimentacaoNormalSerializer(serializers.ModelSerializer):
    motivo = MotivoInclusaoNormalSerializer()

    class Meta:
        model = InclusaoAlimentacaoNormal
        exclude = ('id',)


class InclusaoAlimentacaoContinuaSerializer(serializers.ModelSerializer):
    prioridade = serializers.CharField()
    motivo = MotivoInclusaoContinuaSerializer()
    quantidades_periodo = QuantidadePorPeriodoSerializer(many=True)
    escola = EscolaSimplesSerializer()
    logs = LogSolicitacoesUsuarioSerializer(many=True)
    dias_semana_explicacao = serializers.CharField(
        source='dias_semana_display',
        required=False,
        read_only=True
    )
    id_externo = serializers.CharField()

    class Meta:
        model = InclusaoAlimentacaoContinua
        exclude = ('id',)


class InclusaoAlimentacaoContinuaSimplesSerializer(serializers.ModelSerializer):
    motivo = MotivoInclusaoContinuaSerializer()
    dias_semana_explicacao = serializers.CharField(
        source='dias_semana_display',
        required=False,
        read_only=True
    )
    prioridade = serializers.CharField()

    class Meta:
        model = InclusaoAlimentacaoContinua
        exclude = ('id', 'escola', 'criado_por')


class InclusaoAlimentacaoNormalSimplesSerializer(serializers.ModelSerializer):
    prioridade = serializers.CharField()

    class Meta:
        model = InclusaoAlimentacaoNormal
        exclude = ('id', 'data')


class GrupoInclusaoAlimentacaoNormalSerializer(serializers.ModelSerializer):
    prioridade = serializers.CharField()
    inclusoes = InclusaoAlimentacaoNormalSerializer(many=True)
    escola = EscolaSimplesSerializer()
    quantidades_periodo = QuantidadePorPeriodoSerializer(many=True)
    logs = LogSolicitacoesUsuarioSerializer(many=True)
    id_externo = serializers.CharField()

    class Meta:
        model = GrupoInclusaoAlimentacaoNormal
        exclude = ('id',)


class GrupoInclusaoAlimentacaoNormalSimplesSerializer(serializers.ModelSerializer):
    prioridade = serializers.CharField()

    class Meta:
        model = GrupoInclusaoAlimentacaoNormal
        exclude = ('id', 'criado_por', 'escola')
