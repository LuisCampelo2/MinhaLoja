# Generated by Django 5.1.4 on 2025-01-20 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.CharField(choices=[('eletronicos', 'Eletrônicos'), ('roupas', 'Roupas'), ('livros', 'Livros'), ('esportes', 'Esportes'), ('outros', 'Outros')], default='outros', max_length=50),
        ),
    ]
