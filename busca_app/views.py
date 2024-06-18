from django.shortcuts import render, redirect
from .models import Avaliacoes
from .utils import gerar_avaliacoes
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
import random


def buscar(request):
    num_random = random.randint(1, 7)
    try:
        gerar_avaliacoes(num_random)
    except Exception as e:
        return render(request, 'error.html', {'message': f"Erro ao gerar avaliações: {e}"})
    return redirect('home')

def home(request):
    query = request.GET.get('q')
    data = request.GET.get('data')
    plataforma = request.GET.get('plataforma')
    idioma = request.GET.get('idioma')
    classificacao = request.GET.get('classificacao')
    encontrado_por = request.GET.get('encontrado_por')
    
    avaliacoes = Avaliacoes.objects.all()
    
    if query:
        avaliacoes = avaliacoes.filter(nome__icontains=query)
    if data:
        avaliacoes = avaliacoes.filter(data__date=data)
    if plataforma:
        avaliacoes = avaliacoes.filter(plataforma=plataforma)
    if idioma:
        avaliacoes = avaliacoes.filter(idioma=idioma)
    if classificacao:
        avaliacoes = avaliacoes.filter(classificacao=classificacao)
    if encontrado_por:
        avaliacoes = avaliacoes.filter(encontrado_por_id=encontrado_por)
    
    paginator = Paginator(avaliacoes, 10)
    page_number = request.GET.get('page')
    try:
        avaliacoes = paginator.page(page_number)
    except PageNotAnInteger:
        avaliacoes = paginator.page(1)
    except EmptyPage:
        avaliacoes = paginator.page(paginator.num_pages)
    
    plataformas = Avaliacoes.PLATAFORMA_CHOICES
    idiomas = Avaliacoes.IDIOMA_CHOICES
    classificacoes = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
    usuarios = User.objects.all()
    
    return render(request, 'home.html', {
        'avaliacoes': avaliacoes,
        'plataformas': plataformas,
        'idiomas': idiomas,
        'classificacoes': classificacoes,
        'usuarios': usuarios,
    })
