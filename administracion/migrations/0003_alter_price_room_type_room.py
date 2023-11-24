# Generated by Django 4.2 on 2023-11-23 18:45

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0002_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='room_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type', to='administracion.roomtype', verbose_name='Tipo de Habitación'),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10, verbose_name='Número de habitación')),
                ('status', models.CharField(choices=[('A', 'Activo'), ('I', 'Inactivo'), ('M', 'Mantenimiento')], max_length=1)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_type', to='administracion.roomtype')),
                ('view', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_view', to='administracion.roomview')),
            ],
            managers=[
                ('activas', django.db.models.manager.Manager()),
            ],
        ),
    ]
