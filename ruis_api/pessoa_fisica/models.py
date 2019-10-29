from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=255)
    email = models.EmailField()
    data_nascimento = models.DateField()
    data_cadastro = models.DateField(auto_now_add=True)


class Endereco(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='enderecos')
    logradouro = models.CharField(max_length=255)
    cep = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    uf = models.CharField(max_length=255)


class Telefone(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='telefones')
    numero = models.CharField(max_length=255)
