# Generated by Django 2.2.6 on 2019-12-05 21:15

import uuid

import django.core.validators
import django.db.models.deletion
import django_prometheus.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cardapio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Codae',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
            ],
            options={
                'verbose_name': 'CODAE',
                'verbose_name_plural': 'CODAE',
            },
        ),
        migrations.CreateModel(
            name='DiretoriaRegional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iniciais', models.CharField(blank=True, max_length=10, verbose_name='Iniciais')),
                ('nome', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('codigo_eol', models.CharField(max_length=6, unique=True, validators=[django.core.validators.MinLengthValidator(6)], verbose_name='Código EOL')),
            ],
            options={
                'verbose_name': 'Diretoria regional',
                'verbose_name_plural': 'Diretorias regionais',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Escola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativo', models.BooleanField(default=True, verbose_name='Está ativo?')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('nome', models.CharField(blank=True, max_length=160, verbose_name='Nome')),
                ('codigo_eol', models.CharField(max_length=6, unique=True, validators=[django.core.validators.MinLengthValidator(6)], verbose_name='Código EOL')),
                ('quantidade_alunos', models.PositiveSmallIntegerField(default=1, verbose_name='Quantidade de alunos')),
            ],
            options={
                'verbose_name': 'Escola',
                'verbose_name_plural': 'Escolas',
                'ordering': ('codigo_eol',),
            },
        ),
        migrations.CreateModel(
            name='FaixaIdadeEscolar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('ativo', models.BooleanField(default=True, verbose_name='Está ativo?')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
            ],
            options={
                'verbose_name': 'Idade escolar',
                'verbose_name_plural': 'Idades escolares',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iniciais', models.CharField(blank=True, max_length=10, verbose_name='Iniciais')),
                ('nome', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('diretoria_regional', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='lotes', to='escola.DiretoriaRegional')),
            ],
            options={
                'verbose_name': 'Lote',
                'verbose_name_plural': 'Lotes',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='TipoGestao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('ativo', models.BooleanField(default=True, verbose_name='Está ativo?')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
            ],
            options={
                'verbose_name': 'Tipo de gestão',
                'verbose_name_plural': 'Tipos de gestão',
            },
        ),
        migrations.CreateModel(
            name='TipoUnidadeEscolar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iniciais', models.CharField(blank=True, max_length=10, verbose_name='Iniciais')),
                ('ativo', models.BooleanField(default=True, verbose_name='Está ativo?')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('cardapios', models.ManyToManyField(blank=True, related_name='tipos_unidade_escolar', to='cardapio.Cardapio')),
            ],
            options={
                'verbose_name': 'Tipo de unidade escolar',
                'verbose_name_plural': 'Tipos de unidade escolar',
            },
        ),
        migrations.CreateModel(
            name='Subprefeitura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('diretoria_regional', models.ManyToManyField(blank=True, related_name='subprefeituras', to='escola.DiretoriaRegional')),
                ('lote', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subprefeituras', to='escola.Lote')),
            ],
            options={
                'verbose_name': 'Subprefeitura',
                'verbose_name_plural': 'Subprefeituras',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='PeriodoEscolar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('tipos_alimentacao', models.ManyToManyField(related_name='periodos_escolares', to='cardapio.TipoAlimentacao')),
            ],
            options={
                'verbose_name': 'Período escolar',
                'verbose_name_plural': 'Períodos escolares',
            },
        ),
    ]