# Generated by Django 2.2.8 on 2020-01-22 17:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0009_aluno_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='codigo_eol',
            field=models.CharField(max_length=6, unique=True, validators=[django.core.validators.MinLengthValidator(6)], verbose_name='Código EOL'),
        ),
    ]
