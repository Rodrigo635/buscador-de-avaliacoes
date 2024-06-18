from django.shortcuts import render, redirect, get_object_or_404
from .utils import gerar_avaliacoes
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib import messages
import random

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastrar.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        user = User.objects.filter(username=username).first()

        if user:
            return render(request, 'cadastro.html', {'error': 'Usuário já cadastrado'})
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        return redirect('login')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('password')
        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Usuário ou senha inválidos'})

@login_required
def sair(request):
    logout(request)
    return redirect('home')

#GRUPOS
@login_required
def group_list(request):
    query = request.GET.get('q')
    if query:
        grupos = Group.objects.filter(name__icontains=query)
    else:
        grupos = Group.objects.all()
    paginator = Paginator(grupos, 10)
    page = request.GET.get('page')
    try:
        grupos_paginados = paginator.page(page)
    except PageNotAnInteger:
        grupos_paginados = paginator.page(1)
    except EmptyPage:
        grupos_paginados = paginator.page(paginator.num_pages)

    return render(request, 'grupos.html', {'grupos': grupos_paginados})


@login_required
def group_create(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grupos')
    else:
        form = GroupForm()
    return render(request, 'cadastro.html', {'form': form})

@login_required
def group_update(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('grupos')
    else:
        form = GroupForm(instance=group)
    return render(request, 'editar.html', {'form': form})

@login_required
def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    group.delete()
    messages.info(request, 'Grupo deletada com sucesso.')
    return redirect('grupos')



#USUÁRIOS
@login_required
def user_list(request):
    query = request.GET.get('q')
    if query:
        users = User.objects.filter(username__icontains=query)
    else:
        users = User.objects.all()
    paginator = Paginator(users, 10)
    page = request.GET.get('page')
    try:
        users_paginated = paginator.page(page)
    except PageNotAnInteger:
        users_paginated = paginator.page(1)
    except EmptyPage:
        users_paginated = paginator.page(paginator.num_pages)
    return render(request, 'usuarios.html', {'users': users_paginated})

@login_required
def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = UserForm()
    return render(request, 'cadastro.html', {'form': form})

@login_required
def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = UserForm(instance=user)
    return render(request, 'editar.html', {'form': form})

@login_required
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    messages.info(request, 'Usuário deletado com sucesso.')
    return redirect('users')


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
