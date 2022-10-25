from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    ano_lancamento = models.CharField(max_length=40)
    valor_locacao = models.CharField(max_length=20)

class Locacao(models.Model):
    data_entrega = models.DateField()
    data_locacao = models.DateField() 
    valor = models.CharField(max_length=20)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    filmes = models.ManyToManyField(Filme)

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    categoria = models.ForeignKey(Filme, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome



