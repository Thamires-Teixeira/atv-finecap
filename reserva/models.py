from django.db import models

# Create your models here.
class Reserva(models.Model):
    cnpj = models.CharField(max_length=15)
    nome_empresa = models.CharField(max_length=15)
    categoria_empresa = models.CharField(max_length=150)
    quitado = models.BooleanField(default=False)
    
class Stand(models.Model):
    localizacao = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=10, decimal_places=2)