from django.contrib import admin

from .models import Colaborador  # Importar Classe Colaborador
from .models import Ponto  # Importar Classe Colaborador

admin.site.register(Colaborador) # Registrar Colaborador
admin.site.register(Ponto) # Registrar Colaborador