# Generated by Django 4.0.2 on 2022-05-06 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Carrinho', '0002_carrinho_alter_items_preco_final'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='pertence_pessoa',
        ),
        migrations.AddField(
            model_name='carrinho',
            name='pertence_a',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='carrinho',
            name='status',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
