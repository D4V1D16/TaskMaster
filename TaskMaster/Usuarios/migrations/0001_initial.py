# Generated by Django 5.0.3 on 2024-04-01 20:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tipoUsuario',
            fields=[
                ('idTipo', models.AutoField(primary_key=True, serialize=False)),
                ('nombreTipo', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=100)),
                ('contrasena', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=30)),
                ('tipoUsuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuarios.tipousuario', to_field='nombreTipo')),
            ],
        ),
    ]
