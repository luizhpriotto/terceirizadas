# Generated by Django 2.2.13 on 2020-09-23 11:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dados_comuns', '0022_endereco'),
        ('dieta_especial', '0015_tipocontagem'),
        ('escola', '0016_periodoescolar_horas_atendimento'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='periodo_escolar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='escola.PeriodoEscolar'),
        ),
        migrations.AddField(
            model_name='escola',
            name='endereco',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='dados_comuns.Endereco'),
        ),
        migrations.AddField(
            model_name='escola',
            name='tipos_contagem',
            field=models.ManyToManyField(blank=True, to='dieta_especial.TipoContagem'),
        ),
    ]
