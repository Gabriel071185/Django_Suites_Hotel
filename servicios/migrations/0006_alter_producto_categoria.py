# Generated by Django 4.2 on 2023-10-21 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0005_alter_producto_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(choices=[('comidas', 'comidas'), ('cafeteria', 'cafeteria'), ('bebidas', 'bebidas')], max_length=100, verbose_name='categoria'),
        ),
    ]
