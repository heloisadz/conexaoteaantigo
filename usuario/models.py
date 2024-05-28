from django.db import models

class Usuario (models.Model):

    nome = models.CharField (max_length=100)
    sobrenome = models.CharField (max_length=150)
    CPF = models.CharField(max_length=11, unique=True, default='-', primary_key=True)
    idade = models.IntegerField()
    cidade = models.CharField (max_length = 50)
    estado = models.CharField (max_length = 30)
    identificacao = models.CharField (max_length = 50)
    email = models.CharField (max_length = 200)
    senha = models.CharField (max_length = 50)
# Create your models here.
