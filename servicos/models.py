from django.db import models
from sobreviventes.models import Sobreviventes,Inventario
from .choices import ChoicesCategoriaComercio

class CategoriaComercio(models.Model):
    titulo =models.CharField(max_length=50, choices=ChoicesCategoriaComercio.choices)
    preco = models.IntegerField() 
    
    def __str__(self):
        return self.titulo

class Servico(models.Model):
    titulo = models.CharField(max_length=100)
    sobrevivente = models.ForeignKey(Sobreviventes, on_delete=models.SET_NULL, null=True)
    categoria_comercio = models.ManyToManyField(CategoriaComercio)
    
    
    finalizado =models.BooleanField(default=False)
    
    def __str__(self):
        return self.titulo
    
    
  
    
   
    def preco_total(self):
        preco_total = int(0)
        for categoria in self.categoria_comercio.all():
            preco_total += int(categoria.preco)
            
        return preco_total 