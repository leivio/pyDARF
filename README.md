# pyDARF 

[![PyPI](https://img.shields.io/pypi/pyversions/pubnub.svg)](https://pypi.python.org/pypi/pubnub/)

This is the official pyDARF repository.

pyDARF takes care of the infrastructure and APIs needed for the realtime communication layer of your application. Work on your app's logic and let PubNub handle sending and receiving data across the world in less than 100ms.


## Samples

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

## Deploy with Flask

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
