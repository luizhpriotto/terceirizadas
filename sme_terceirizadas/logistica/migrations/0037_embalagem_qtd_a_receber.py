# Generated by Django 2.2.13 on 2021-06-08 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistica', '0036_auto_20210526_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='embalagem',
            name='qtd_a_receber',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='Quantidade a receber faltante'),
        ),
    ]
