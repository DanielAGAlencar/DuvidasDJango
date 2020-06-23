from django.db import models


class Tipo(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


# Create your models here.
class Duvida(models.Model):
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=20)
    data = models.CharField(max_length=20)
    nome_aluno = models.CharField(max_length=100)
    nome_professor = models.CharField(max_length=100)
    tipo = models.ForeignKey(Tipo, on_delete = models.SET_NULL, null = True)

    def __str__(self):
        return self.descricao
