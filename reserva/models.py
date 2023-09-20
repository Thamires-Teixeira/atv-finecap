from django.db import models

class Stand(models.Model):
    localizacao = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self) -> str:
        return self.localizacao

class Reserva(models.Model):
    cnpj = models.CharField(max_length=15)
    nome_empresa = models.CharField(max_length=15)
    categoria_empresa = models.CharField(max_length=150)
    quitado = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)
    stand = models.ForeignKey(Stand, on_delete=models.CASCADE)

    def _str_(self) -> str:
        return self.stand.localizacao