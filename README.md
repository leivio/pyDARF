# pyDARF

[![PyPI](https://img.shields.io/pypi/pyversions/pubnub.svg)](https://pypi.python.org/pypi/pubnub/)

This is the official pyDARF repository.

pyDARF takes simple lib for generation the barcode and digitable line layer of your application. Used to pay taxes from the Brazilian Federal Revenue.
Standard followed by the FEBRABAN document and carried out tests with apps from banks in Brazil.

## example

```python
from darf import Darf

codigoreceita       = '0211'
codigocontribuinte  =  '66342797000113'
vencimento          = '2021-03-18'
apuracao            = '2021-02-28'
valor               =  129,33

codigobarras, linhadigitavel, encoded_string = Darf.codigo_de_barras(codigoreceita, codigocontribuinte, vencimento, apuracao, valor)

print(codigobarras)
print(linhadigitavel)
print(encoded_string)

```

## example with Flask

```python
from flask import Flask, request, jsonify
from darf import Darf


app = Flask(__name__)

@app.route('/')
def darf():
    if len(request.args) < 3:
        return 'paramentros vazio'
    else:
        codigoreceita      = request.args.get('codigoreceita')
        codigocontribuinte = request.args.get('codigocontribuinte')
        vencimento         = request.args.get('vencimento')
        apuracao           = request.args.get('apuracao')
        valor              = request.args.get('valor')
        codigobarras, linhadigitavel, encoded_string = Darf.codigo_de_barras(codigoreceita, codigocontribuinte, vencimento, apuracao, valor)
        #retorno
        response = {"codigoBarras": codigobarras,"linhadigitavel": linhadigitavel, "img": encoded_string.decode("utf-8") }
        return jsonify(response)

if __name__ == '__main__':
    app.run()

# http://127.0.0.1:5000?codigoreceita=0211&codigocontribuinte=66342797000113&vencimento=2021-03-18&apuracao=2021-02-28&valor=123.49

```

## Support

If you **need help** or have a **general question**, contact leivio@yahoo.com.br

## Start project

Create the environment:

```bash
python3 -m venv venv
. venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start app:

```bash
flask run
```
