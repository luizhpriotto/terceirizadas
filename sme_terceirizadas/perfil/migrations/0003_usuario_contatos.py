# Generated by Django 2.2.6 on 2019-12-13 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dados_comuns', '0005_auto_20191210_1540'),
        ('perfil', '0002_auto_20191213_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='contatos',
            field=models.ManyToManyField(blank=True, to='dados_comuns.Contato'),
        ),
    ]