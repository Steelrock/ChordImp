#!/usr/bin/python
# -*- coding: UTF-8 -*-

import requests
import json



dadosCliente = {
  "name": "Raspberry PI",
  "chipset": "AMD 790FX",
  "mac": "FF:FF:FF:FF:FF:FF",
  "serial": "C210",
  "processor": "Intel I3",
  "channel": "Ethernet",
  "client_time": 1317427200,
  "location": "0,0"
}

Token = ""
dadosServico = {
  "services": [
    {
      "name": "ascascascascscacaafasssssssssssssssssssssssssssssssssssssssss",
      "parameters": {
        "PArametro": "batata"
      },
      "return_type": "float"
    }
  ],
  "tokenId": "",
  "timestamp": 1317427200
}


dadosData = {
  "token": "1d5dec12f0a2c96bd9a70dab08a77963",
  "data": [
    {
      "service_id": 0,
      "data_values": {
        "batata": "EU estive aquiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
      }
    }
  ]
}

class AutoRegistro(object):
  def __init__(self, URL, data):
    self.URL = URL
    self.data = data
    self.token = ""

    if (self.URL == "http://homol.redes.unb.br/uiot-raise/client/register"): self.RegistrarCliente(self.data)
    if (self.URL == "http://homol.redes.unb.br/uiot-raise/service/register"): self.RegistrarServico(self.data)
    if (self.URL == "http://homol.redes.unb.br/uiot-raise/data/register"): self.RegistrarData(self.data)



  def RegistrarCliente(self, data):
    # Registro de clientes (gera um token)
    # Gera um requisicao HTTP (metodo POST) e grava seu retorno em "r"
    r = requests.post(self.URL, data=json.dumps(data))
    print(r.content)

    self.token = self.IdentificarToken(r)


  def RegistrarServico(self, data):
    # Registro de Servico
    # Gera um requisicao HTTP (metodo POST) e grava seu retorno em "r"
    r = requests.post(self.URL, data = json.dumps(data))



  def RegistrarData(self, data):
    # Registro de Servico
    # Gera um requisicao HTTP (metodo POST) e grava seu retorno em "r"
    r = requests.post(self.URL, data=json.dumps(data))

  def MostrarClientes(self):
    # Mostra os clientes Registrados
    # Gera um requisicao HTTP (metodo GET) e grava seu retorno em "r"
    r = requests.get("http://homol.redes.unb.br/uiot-raise/client/list?tokenId=" + str(self.token))
    print (r.content)

  def MostrarServicos(self):
    # Mostra os Serviços Registrados
    # Gera um requisicao HTTP (metodo GET) e grava seu retorno em "r"
    r = requests.get("http://homol.redes.unb.br/uiot-raise/service/list?tokenId=" + str(self.token))
    print (r.content)

  def MostrarData(self):
    # Mostra os Serviços Registrados
    # Gera um requisicao HTTP (metodo GET) e grava seu retorno em "r"
    r = requests.get("http://homol.redes.unb.br/uiot-raise/data/list?tokenId=" + str(self.token))
    print (r.content)

  def IdentificarToken(self,r):
    ini = r.content.find("\"tokenId\": ") + 12
    token = ""
    for i in range(32):
      token = token + r.content[ini + i]
    return token
  def GetCurrentToken(self):
    print ("O token que vc deve usar é: %s" %(self.token))
    return self.token

# registrar Cliente AND Ver todos os Clientes registrados
A1 = AutoRegistro("http://homol.redes.unb.br/uiot-raise/client/register", dadosCliente)

# registrar Serviços AND Ver todos os Serviços registrados
#A1 = AutoRegistro("http://homol.redes.unb.br/uiot-raise/service/register", dadosServico)
#A1.MostrarServicos()

# registrar Dados AND Ver todoos os Dados registrados
#A1 = AutoRegistro("http://homol.redes.unb.br/uiot-raise/service/register", dadosData)
#A1.MostrarServicos()


