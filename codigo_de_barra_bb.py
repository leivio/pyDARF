#!/usr/bin/env python
# encoding: utf-8

import sys
from PIL import Image, ImageDraw, ImageFont


class Codigodebarra:
    def __init__(self):
        pass

    def getcodbarra(self, valor, posX=150, posY=0, height=60):

        # padrão 2 por 5 intercalado ( utilizado em boletos bancários )
        padrao = ('00110', '10001', '01001', '11000', '00101',
                  '10100', '01100', '00011', '10010', '01010')

        # criando imagem
        imagem = Image.new('RGB', (750, 80), 'white')
        draw = ImageDraw.Draw(imagem)

        # verificando se o conteudo para gerar barra é impar, se for,
        # adiciona 0 no inicial para fazer intercalação em seguida dos pares

        if (len(valor) % 2) != 0:
            valor = '0' + valor

        # faz intercalação dos pares
        l = ''
        for i in range(0, len(valor), 2):
            p1 = padrao[int(valor[i])]
            p2 = padrao[int(valor[i + 1])]
            for p in range(0, 5):
                l += p1[:1] + p2[:1]
                p1 = p1[1:]
                p2 = p2[1:]

        # gerando espaços e barras
        barra = True
        b = ''

        # P = preto
        # B = banco

        for i in range(0, len(l)):
            if l[i] == '0':
                if barra:
                    b += 'P'
                    barra = False
                else:
                    b += 'B'
                    barra = True
            else:
                if barra:
                    b += 'PPP'
                    barra = False
                else:
                    b += 'BBB'
                    barra = True

        # concatena inicio e fim
        b = 'PBPB' + b + 'PPPBP'

        # P = preto
        # B = banco

        print("b: ", b)

        # percorre toda a string b e onde for P pinta de preto, onde for B pinta de banco

        for i in range(0, len(b)):
            if b[i] == 'P':
                draw.line((posX, posY, posX, posY + height), 'black')
            else:
                draw.line((posX, posY, posX, posY + height), 'white')
            posX += 1
        return imagem
