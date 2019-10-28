from django.db import models


class Pessoa(models.Model):
    nome = models.CharField()
    cpf = models.CharField()
    email = models.EmailField()
    data_nascimento = models.DateField()
    data_cadastro = models.DateField(auto_now_add=True)


class Endereco(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    logradouro = models.CharField()
    cep = models.CharField()
    bairro = models.CharField()
    cidade = models.CharField()
    uf = models.CharField()


class Telefone(models.Model):
    numero = models.CharField()