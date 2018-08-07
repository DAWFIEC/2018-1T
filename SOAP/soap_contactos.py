import os
from flaskext.enterprise import Enterprise
from flask import Flask, render_template


app = Flask(__name__)

enterprise = Enterprise(app)
String = enterprise._sp.String
Integer = enterprise._sp.Integer
Boolean = enterprise._sp.Boolean
Array = enterprise._scls.Array

contactos = {
    "claro": {
        "numero": "+5939 673 3278",
        "contacto": "Carlos Espin"
    },
    "movistar": {
        "numero": "+5938 782 0293",
        "contacto": "Andrea Noboa"
    },
    "emapag": {
        "numero": "+5934 234 2901",
        "contacto": "Carolina Barios"
    }
}


class Service(enterprise.SOAPService):

    __soap_target_namespace__ = 'TodosMisServicios'
    __soap_server_address__ = '/tms-soap'

    @enterprise.soap(String,  _returns=String)
    def obtenerContactoClaro(self, servicios):
        print(self,servicios)
        return "nombre:%s,contacto:%s" % (contactos["claro"]["contacto"], contactos["claro"]["numero"]) 

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.debug = True
    app.run(host='127.0.0.1', port=port)