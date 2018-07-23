import os
from flask import Flask, json, Response, render_template, request
from pymongo import MongoClient # Database connector
from bson.objectid import ObjectId # For ObjectId to work


client = MongoClient('mongodb://aavendan86:mlab2018@ds143461.mlab.com:43461/todosmisservicios',43461)
db = client.todosmisservicios    #Select the database

usuarios = [
        {
            "id":"C001",
            "nombre":"Pepita Suárez",
            "direccion": "Sauces II"
        },
        {
            "id":"C002",
            "nombre":"Andrés Medina",
            "direccion": "Los Vergeles"
        }
    ]

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html", usuarios=usuarios)

@app.route("/listar-cuentas/<id>") 
def cuentas(id):

    resultado = dict()

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