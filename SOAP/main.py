import os
from flask import Flask, render_template
from suds.client import Client

app = Flask(__name__)

@app.route('/')
def pageIndex():
    client = Client(url='http://127.0.0.1:5000/tms-soap?wsdl')
    request = client.factory.create('tns:obtenerContactoClaro')
    request.servicios = 'claro'
    response = client.service.obtenerContactoClaro(request)


    valor1, valor2 = response.split(",")
    nombre= valor1.split(":")[1]
    numero= valor2.split(":")[1]

    contacto = {"nombre":nombre, "numero": numero, "servicio":"claro"}
    return render_template("index.html", contacto = contacto)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.debug = True
    app.run(host='127.0.0.1', port=port)