# Generated by Django 2.2.10 on 2020-07-01 22:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0038_auto_20200701_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anexorespostaanalisesensorial',
            name='resposta_analise_sensorial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anexos', to='produto.RespostaAnaliseSensorial'),
        ),
    ]
