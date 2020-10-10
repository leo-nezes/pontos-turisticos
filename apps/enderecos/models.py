from django.db import models


class Endereco(models.Model):
    linha1 = models.CharField(max_length=150) #Linha para digitar o endereço
    linha2 = models.CharField(max_length=150, null=True, blank=True) #Linha para digitar o endereço
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=70)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.linha1
