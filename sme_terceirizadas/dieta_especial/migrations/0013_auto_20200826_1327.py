# Generated by Django 2.2.13 on 2020-08-26 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dieta_especial', '0012_auto_20200423_1505'),
        ('produto', '__first__'),
    ]

    operations = [
        migrations.AlterField(
            model_name='substituicaoalimento',
            name='substitutos',
            field=models.ManyToManyField(blank=True, related_name='substitutos', to='produto.Produto'),
        ),
    ]