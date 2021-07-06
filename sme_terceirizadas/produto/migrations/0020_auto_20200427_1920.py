# Generated by Django 2.2.8 on 2020-04-27 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0019_auto_20200426_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='informacaonutricional',
            name='medida',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='informacoesnutricionaisdoproduto',
            name='quantidade_porcao',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
        migrations.AlterField(
            model_name='informacoesnutricionaisdoproduto',
            name='valor_diario',
            field=models.DecimalField(decimal_places=2, max_digits=2),
        ),
    ]
