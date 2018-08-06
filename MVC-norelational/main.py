import os
from flask import Flask, json, Response, render_template, request
from pymongo import MongoClient # Database connector
from bson.objectid import ObjectId # For ObjectId to work

#client = MongoClient('mongodb://aavendan86:mlab2018@ds143461.mlab.com:43461/todosmisservicios',43461)
client = MongoClient('mongodb://localhost:27017/')
db = client.todosmisservicios    #Select the database

app = Flask(__name__)

@app.route('/')
def main():
    usuarios = db.usuarios.find()
    return render_template("index.html", usuarios=usuarios)

@app.route("/listar-cuentas/<id>") 
def cuentas(id):

    resultado = dict()
    usuarios = db.usuarios.find()

    for usuario in usuarios:
        if usuario["id"] == id:
            usuario_activo = usuario

            cuentas_usuario = db.cuentas.find({"colaborador": id})
            for cuenta in cuentas_usuario:
                lista = resultado.get(cuenta['ubicacion'], [])
                lista.append(cuenta['nombre'])
                resultado[cuenta['ubicacion']] = lista
                
    return render_template("cuentas.html", usuario=usuario_activo, resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)