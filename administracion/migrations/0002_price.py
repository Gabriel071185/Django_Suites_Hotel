# Generated by Django 4.2 on 2023-11-18 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField(verbose_name='Desde: ')),
                ('date_to', models.DateField(verbose_name='Hasta: ')),
                ('price', models.DecimalField(decimal_places=2, help_text='Usar punto (.) para los decimales y no usar separador de miles', max_digits=10, verbose_name='Valor por noche (AR$)')),
                ('room_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.roomtype', verbose_name='Tipo de Habitación')),
                ('room_view', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.roomview', verbose_name='Vista de la Habitación')),
            ],
        ),
    ]