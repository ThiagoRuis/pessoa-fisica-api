from rest_framework import serializers
from .models import Pessoa, Endereco, Telefone


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id', 'pessoa', 'logradouro', 'cep', 'bairro', 'cidade', 'uf', "pessoa"]
        read_only_fields = ['id']


class TelefoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telefone
        fields = ['id', 'numero', "pessoa"]
        read_only_fields = ['id']


class PessoaSerializer(serializers.ModelSerializer):
    enderecos = EnderecoSerializer(many=True)
    telefones = TelefoneSerializer(many=True)
    
    
    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'cpf', 'email', 'data_nascimento', 'data_cadastro', 'enderecos', 'telefones']
        read_only_fields = ['id', 'data_cadastro']