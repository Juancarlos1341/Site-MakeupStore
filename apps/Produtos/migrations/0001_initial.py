# Generated by Django 4.0.2 on 2022-04-20 20:56

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrossel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_carrossel', models.CharField(max_length=100)),
                ('carrosel_1', models.ImageField(upload_to='Carrosel/%d')),
                ('carrosel_2', models.ImageField(upload_to='Carrosel/%d')),
                ('carrosel_3', models.ImageField(upload_to='Carrosel/%d')),
                ('publicar', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=240)),
                ('imagem', models.ImageField(upload_to='categoria/%d')),
                ('publicada', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_produto', models.CharField(max_length=240)),
                ('preco', models.CharField(max_length=100)),
                ('descricao', models.TextField(max_length=240)),
                ('estoque', models.IntegerField()),
                ('imagem_produto', models.ImageField(blank=True, upload_to='produtos/%d')),
                ('ativo', models.BooleanField(default=True)),
                ('data_de_criacao', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('promocao', models.BooleanField(default=False)),
                ('oferta', models.BooleanField(default=False)),
                ('aparecer_no_desteque', models.BooleanField(default=False)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produtos.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Dicas_produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_da_dica', models.CharField(max_length=100)),
                ('imagem', models.ImageField(blank=True, upload_to='dicas/%d')),
                ('descricao', models.TextField(max_length=255)),
                ('publicar_dica', models.BooleanField(default=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Produtos.produtos')),
            ],
        ),
    ]
