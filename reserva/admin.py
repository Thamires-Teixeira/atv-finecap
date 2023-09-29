from django.contrib import admin
from .models import Reserva, Stand
@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display=('nome_empresa','cnpj','categoria_empresa')

@admin.register(Stand)
class StandAdmin(admin.ModelAdmin):
    list_display=("localizacao", "valor")

