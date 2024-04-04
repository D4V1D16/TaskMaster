# Generated by Django 5.0.3 on 2024-04-03 14:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('idTarea', models.IntegerField(primary_key=True, serialize=False)),
                ('nombreTarea', models.CharField(max_length=30)),
                ('descripcion', models.TextField()),
                ('fechaComienzo', models.DateField()),
                ('fechaVencimiento', models.DateTimeField()),
                ('usuarioAsignado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]