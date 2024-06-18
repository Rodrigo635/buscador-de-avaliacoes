# Generated by Django 5.0.6 on 2024-05-29 00:58

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
            name='Avaliacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('texto', models.TextField()),
                ('plataforma', models.CharField(choices=[('plataforma 1', 'plataforma 1'), ('plataforma 2', 'plataforma 2'), ('plataforma 3', 'plataforma 3'), ('plataforma 4', 'plataforma 4'), ('plataforma 5', 'plataforma 5')], max_length=100)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('classificacao', models.IntegerField()),
                ('idioma', models.CharField(choices=[('pt-br', 'Portugues Brasileiro'), ('pt', 'Portugues'), ('ing', 'Ingles'), ('esp', 'Espanhol'), ('itn', 'Italiano')], max_length=100)),
                ('encontrado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]