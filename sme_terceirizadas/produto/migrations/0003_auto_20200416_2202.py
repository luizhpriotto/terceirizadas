# Generated by Django 2.2.8 on 2020-04-17 01:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_auto_20200416_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informacoesnutricionaisdoproduto',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.Produto'),
        ),
    ]
