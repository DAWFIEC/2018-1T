from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

servicios = [
{"id":"0001","nombre":"Claro", "direccion":"Guayaquil", "telefono":"2018-03-21"},
{"id":"0002","nombre":"Movistar", "direccion":"Manta", "telefono":"2018-04-08"},
{"id":"0003","nombre":"EMAPAG", "direccion":"Guayaquil", "telefono":"2018-06-01"}
]

class ServiciosList(Resource):
    def get(self):
        return {"lista": servicios, "status":"200"}

class Servicios(Resource):
    def get(self, servicio_id):
        for servicio in servicios:
            if servicio_id in servicio['id']:
                return {"servicio": servicio, "status":"200"}
        return {"status":"400"}

    def post(self, servicio_id):
        for servicio in servicios:
            if servicio_id in servicio['id']:
                return {"status":"400"}

        servicio = dict()
        servicio[servicio_id] = request.form['nombre']
        servicios.append(servicio)

        return {"servicio": servicio, "status":"200"}

    def put(self, servicio_id):
        for servicio in servicios:
            if servicio_id in servicio['id']:
                servicio[servicio_id] = request.form['nombre']
                return {"servicio": servicio, "status":"200"}
        return {"status":"400"}

    def delete(self, servicio_id):
        for servicio in servicios:
            if servicio_id in servicio['id']:
                servicios.remove(servicio)
                return {"status":"200"}
        return {"status":"400"}

api.add_resource(Servicios, '/<string:servicio_id>')
api.add_resource(ServiciosList, '/')



if __name__ == '__main__':
    app.run(debug=True, port=5050)