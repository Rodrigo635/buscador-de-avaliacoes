from django.db import models
from django.contrib.auth.models import User

class Avaliacoes(models.Model):
    PLATAFORMA_CHOICES = [
        ('plataforma 1', 'Plataforma 1'),
        ('plataforma 2', 'Plataforma 2'),
        ('plataforma 3', 'Plataforma 3'),
        ('plataforma 4', 'Plataforma 4'),
        ('plataforma 5', 'Plataforma 5'),
    ]

    IDIOMA_CHOICES = [
        ('pt-br', 'Português Brasileiro'),
        ('pt', 'Português'),
        ('ing', 'Inglês'),
        ('esp', 'Espanhol'),
        ('itn', 'Italiano'),
    ]

    nome = models.CharField(max_length=100, verbose_name="Nome")
    texto = models.TextField(verbose_name="Texto")
    plataforma = models.CharField(max_length=50, choices=PLATAFORMA_CHOICES, verbose_name="Plataforma")
    data = models.DateTimeField(auto_now_add=True, verbose_name="Data")
    classificacao = models.IntegerField(verbose_name="Classificação")
    idioma = models.CharField(max_length=20, choices=IDIOMA_CHOICES, verbose_name="Idioma")
    encontrado_por = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Encontrado por")

    def __str__(self):
        return self.nome
