# Generated by Django 2.2.8 on 2020-01-06 19:29

import environ
from django.db import migrations

ROOT_DIR = environ.Path(__file__) - 2

sql_path = ROOT_DIR.path('sql', '0001_solicitacoes_dieta_ativas_inativas_por_aluno.sql')
with open(sql_path, 'r') as f:
    sql = f.read()


class Migration(migrations.Migration):
    dependencies = [
        ('dieta_especial', '0007_solicitacaodietaespecial_ativo'),
    ]

    operations = [
        migrations.RunSQL(
            sql,
            "DROP VIEW dietas_ativas_inativas_por_aluno;"
        )
    ]
