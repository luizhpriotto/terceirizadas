# Generated by Django 2.2.13 on 2021-06-03 16:57

from django.db import migrations
import django_xworkflows.models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0048_auto_20210316_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homologacaodoproduto',
            name='status',
            field=django_xworkflows.models.StateField(max_length=45, workflow=django_xworkflows.models._SerializedWorkflow(initial_state='RASCUNHO', name='HomologacaoProdutoWorkflow', states=['RASCUNHO', 'CODAE_PENDENTE_HOMOLOGACAO', 'CODAE_HOMOLOGADO', 'CODAE_NAO_HOMOLOGADO', 'CODAE_QUESTIONADO', 'CODAE_PEDIU_ANALISE_SENSORIAL', 'TERCEIRIZADA_CANCELOU', 'HOMOLOGACAO_INATIVA', 'CODAE_SUSPENDEU', 'ESCOLA_OU_NUTRICIONISTA_RECLAMOU', 'CODAE_PEDIU_ANALISE_RECLAMACAO', 'TERCEIRIZADA_RESPONDEU_RECLAMACAO', 'CODAE_AUTORIZOU_RECLAMACAO', 'TERCEIRIZADA_CANCELOU_SOLICITACAO_HOMOLOGACAO'])),
        ),
    ]