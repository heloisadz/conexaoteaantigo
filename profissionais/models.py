from django.db import models

class Profissionais (models.Model):
    especialidade = models.CharField (max_length=100)
    nome = models.CharField (max_length=100)
    crm = models.CharField (max_length=50)
    endereco = models.CharField (max_length = 200)
    descricao = models.CharField (max_length = 200)
    telefone = models.CharField (max_length=12)
