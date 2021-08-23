# encoding: utf-8

import re
from datetime import date, datetime
import base64
from io import BytesIO
from codigo_de_barra_bb import Codigodebarra

class Darf:
    def __init__(self):
        pass

    @staticmethod
    def str_to_zero(string, tamanho,esquerda = True):
      str = string
      while len(str) < tamanho:
        if esquerda:
          str = '0' + str
        else:
          str = str + '0'
      return str

    @staticmethod
    def calcula_mod_10(number):
        total = 0
        digits = list(map(int, str(number)))
        reversedDigits = digits[::-1]
        total = 0
        for position, digit in enumerate(reversedDigits):
            if (position + 1) % 2 == 1:
                digit *= 2
                if digit > 9: digit -= 9
            total += digit
        total = total * 9
        return str(total % 10)

    @staticmethod
    def codigo_de_barras(codigoreceita, codigocontribuinte, datavencimento, dataapuracao, valor):

        # 8 - Arrecadação | 5 - Órgãos Governamentais | 6 - - Valor a ser cobrado efetivamente em reais
        pre = '856'
        # 0064 - DARF IRRF | 0179 - FGTS | 0239 - FGTS Rescisório | 0328 - Simples Nacional
        orgao = '0064'

        _valor = Darf.str_to_zero(valor.replace('.', ''), 11)

        # Data Zero
        datazero = datetime.strptime('2018-04-06', '%Y-%m-%d')

        # Data final '2017-05-05'
        d2 = datetime.strptime(datavencimento, '%Y-%m-%d')

        # Data inicial '2017-05-05'
        d1 = datetime.strptime(dataapuracao, '%Y-%m-%d')

        # Realizamos o calculo da quantidade de dias
        _apuracao = abs((d1 - datazero).days)
        _vencimento = abs((d2 - datazero).days)
        _codigocontribuinte = codigocontribuinte
        if len(codigocontribuinte) == 14:
          _codigocontribuinte = '1' + _codigocontribuinte[0:12]
          _codigoreceita = Darf.str_to_zero(codigoreceita, 4)
        else:
          _codigocontribuinte = '0' + _codigocontribuinte
          _codigoreceita = Darf.str_to_zero(codigoreceita, 5)

        print("_valor: " + _valor)
        print("_apuracao: " + str(_apuracao))
        print("_vencimento: " + str(_vencimento))
        print("_codigocontribuinte: " + _codigocontribuinte)

        # Juncao dos codigos
        codigobarras = pre + _valor + orgao + str(_vencimento) + _codigocontribuinte + _codigoreceita + str(_apuracao)

        print("codigobarras1: " + codigobarras)


        digito0 = Darf.calcula_mod_10(codigobarras)
        
        print("digito0: " + digito0)

        codigobarras = codigobarras[:3] + digito0 + codigobarras[3:]
        print("codigobarras2: " + codigobarras)

        PreFor1 = codigobarras[0:11]
        PreFor1 = PreFor1 + '-' + Darf.calcula_mod_10(PreFor1)

        PreFor2 = codigobarras[11:22]
        PreFor2 = PreFor2 + '-' + Darf.calcula_mod_10(PreFor2)

        PreFor3 = codigobarras[22:33]
        PreFor3 = PreFor3 + '-' + Darf.calcula_mod_10(PreFor3)

        PreFor4 = codigobarras[33:44]
        PreFor4 = PreFor4 + '-' + Darf.calcula_mod_10(PreFor4)

        linhadigitavel = PreFor1 + ' ' + PreFor2 + ' ' + PreFor3 + ' ' + PreFor4
        print("linhadigitavel: " + linhadigitavel)


        barra = Codigodebarra()
        # formato que deseja salvar a imagem (PNG,GIF)
        tipo = 'PNG'
        # retornando uma imagem a partir do código de barra
        image = barra.getcodbarra(codigobarras)
        # salvando imagem do tipo informado na variavel tipo
        # image.save('%s.%s' % (codigocontribuinte, tipo))

        #Convertendo base64
        buffered = BytesIO()
        # image.save(buffered, format="JPEG")
        encoded_string = base64.b64encode(buffered.getvalue())

        return codigobarras, linhadigitavel, encoded_string
