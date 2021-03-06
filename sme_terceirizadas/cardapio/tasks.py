import datetime
import logging

from celery import shared_task
from django.db.models import Q

from ..escola.constants import PERIODOS_ESPECIAIS_CEI_CEU_CCI
from ..escola.models import EscolaPeriodoEscolar, PeriodoEscolar, TipoUnidadeEscolar
from .models import VinculoTipoAlimentacaoComPeriodoEscolarETipoUnidadeEscolar

logger = logging.getLogger('sigpae.taskCardapio')


@shared_task(
    retry_backoff=5,
    retry_kwargs={'max_retries': 2},
)
def ativa_desativa_vinculos_alimentacao_com_periodo_escolar_e_tipo_unidade_escolar():
    """O sistema assume que todas as escolas tem todos os períodos.

    Essa função ativa/desativa dinamicamente o vínculo entre TipoUE e Períodos escolares
    caso tenha ou não algum aluno em algum periodo escolar.

    OBS: período PARCIAL funciona somente para CEI CEU, CEI e CCI, para mais detalhes,
    vide `tem_somente_integral_e_parcial()` em TipoUnidadeEscolar
    """
    logger.debug(f'Iniciando task ativa_desativa_vinculos_alimentacao_com_periodo_escolar_e_tipo_unidade_escolar'
                 f' às {datetime.datetime.now()}')

    for tipo_unidade in TipoUnidadeEscolar.objects.all():
        # atualiza com base nos dados da api do EOL
        for periodo_escolar in PeriodoEscolar.objects.all():
            vinculo, created = VinculoTipoAlimentacaoComPeriodoEscolarETipoUnidadeEscolar.objects.get_or_create(
                tipo_unidade_escolar=tipo_unidade, periodo_escolar=periodo_escolar)
            tem_alunos_neste_periodo_e_tipo_ue = EscolaPeriodoEscolar.objects.filter(
                periodo_escolar=periodo_escolar,
                escola__tipo_unidade=tipo_unidade,
                quantidade_alunos__gte=1
            ).exists()
            vinculo.ativo = tem_alunos_neste_periodo_e_tipo_ue
            vinculo.save()

        if tipo_unidade.tem_somente_integral_e_parcial:
            # deve ter periodo INTEGRAL E PARCIAL somente
            periodos_escolares = PERIODOS_ESPECIAIS_CEI_CEU_CCI
            vinculo_tipo_unidade = VinculoTipoAlimentacaoComPeriodoEscolarETipoUnidadeEscolar.objects.filter(
                tipo_unidade_escolar=tipo_unidade
            )
            vinculo_tipo_unidade.filter(periodo_escolar__nome__in=periodos_escolares).update(ativo=True)
            vinculo_tipo_unidade.filter(~Q(periodo_escolar__nome__in=periodos_escolares)).update(ativo=False)
