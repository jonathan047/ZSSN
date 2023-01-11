from django.db import models
from sobreviventes.models import Sobreviventes,Inventario

class Sobreviventes(models.Model):
    sobreviventes = models.CharField(max_length= 50)
    infectados = models.IntegerField()
    n_infectados = models.IntegerField()
    agua = models.IntegerField()
    alimento = models.IntegerField()
    medicamento= models.IntegerField()
    municao = models.IntegerField()
    
    def __str__(self):
        return self.infectados
    
class Pontos(models.Model):
    pontos =models.IntegerField() 
    infectados = models.ForeignKey(Sobreviventes,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.pontos
