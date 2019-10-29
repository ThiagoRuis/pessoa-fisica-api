from django.shortcuts import render
from rest_framework import viewsets, status, mixins
from rest_framework.response import Response

from .models import Pessoa, Endereco, Telefone
from .serializers import PessoaSerializer, EnderecoSerializer, TelefoneSerializer

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()    
    serializer_class = PessoaSerializer


class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()    
    serializer_class = EnderecoSerializer


class TelefoneViewSet(viewsets.ModelViewSet):
    queryset = Telefone.objects.all()    
    serializer_class = TelefoneSerializer