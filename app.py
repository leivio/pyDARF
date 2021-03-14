from flask import Flask, request, jsonify
from darf import Darf
from codigo_de_barra_bb import Codigodebarra
import base64
from io import BytesIO

app = Flask(__name__)


@app.route('/')
def Root():
    return 'pyDarf - Gerador Linha digitavel e imagem do Codigo de Barras de Documentos DARF Receita Federal'

@app.route('/darf')
def darf():
    if len(request.args) < 3:
        return 'paramentros vazio'
    else:
        codigoreceita      = request.args.get('codigoreceita')
        codigocontribuinte = request.args.get('codigocontribuinte')
        vencimento         = request.args.get('vencimento')
        apuracao           = request.args.get('apuracao')
        valor              = request.args.get('valor')
        codigobarras, linhadigitavel = Darf.codigo_de_barras(codigoreceita, codigocontribuinte, vencimento, apuracao, valor)

        barra = Codigodebarra()
        # formato que deseja salvar a imagem (PNG,GIF)
        tipo = 'PNG'
        # retornando uma imagem a partir do código de barra
        image = barra.getcodbarra(codigobarras)
        # salvando imagem do tipo informado na variavel tipo
        #image.save('%s.%s' % (codigo, tipo))

        #Convertendo base64
        buffered = BytesIO()
        image.save(buffered, format="JPEG")
        encoded_string = base64.b64encode(buffered.getvalue())
        #retorno
        response = {"codigoBarras": codigobarras,"linhadigitavel": linhadigitavel, "img": encoded_string.decode("utf-8") }
        return jsonify(response)

if __name__ == '__main__':
    app.run()

# http://127.0.0.1:5000/darf?codigoreceita=0211&codigocontribuinte=66342797000113&vencimento=2021-03-18&apuracao=2021-02-28&valor=123.49