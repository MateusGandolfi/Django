from django.urls import path
from django.contrib import admin
from app_cad_usuarios import views

urlpatterns = [
    # rota, view responsavel, nome de referencia
    # painel de adm
    path('admin/', admin.site.urls),
    # usuarios.com
    path('', views.home, name='home'),
    # usuarios.com/usuarios
    path('usuarios/',views.usuarios, name='listagem_usuarios')
]