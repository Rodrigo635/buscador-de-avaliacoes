from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('buscar/', views.buscar, name='buscar'),
    path('login/', views.login, name='login'),
    path('cadastrar/', views.cadastro, name='cadastrar'),
    path('logout/', views.sair, name='sair'),

    path('groupos/', views.group_list, name='grupos'),
    path('cadastro-grupo/', views.group_create, name='cadastro_grupo'),
    path('groups/<int:pk>/update/', views.group_update, name='editar_grupo'),
    path('deletar_grupo/<int:pk>/', views.group_delete, name='deletar_grupo'),

    path('users/', views.user_list, name='users'),
    path('cadastro-user/', views.user_create, name='cadastro_user'),
    path('users/<int:pk>/update/', views.user_update, name='user_update'),
    path('users/<int:pk>/delete/', views.user_delete, name='user_delete'),
]
