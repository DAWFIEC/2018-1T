from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

aeropuertos = {}

class Aeropuerto(Resource):
    def get(self, atoId):
        return {atoId: aeropuertos[atoId]}

    def put(self, atoId):
        aeropuertos[atoId] = request.form['data']
        return {atoId: aeropuertos[atoId]}

api.add_resource(Aeropuerto, '/aeropuertos/<string:atoId>')

if __name__ == '__main__':
    app.run(debug=True)
