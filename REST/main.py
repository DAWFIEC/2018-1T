import os
from flask import Flask, json, Response, render_template, request, redirect
import requests

app = Flask(__name__)

@app.route('/')
def main():
    servicios = requests.get('http://localhost:5050/').json()
    return render_template("index.html", servicios=servicios["lista"])

@app.route('/ver/<id>')
def ver(id):
	resultado = requests.get('http://localhost:5050/'+str(id)).json()
	print(resultado)
	return render_template("servicio.html", servicio=resultado['servicio'])

@app.route('/accion/<id>', methods=['post', 'get'])
def accion(id):
	if request.form.get('accion') == 'Editar':
		servicios = requests.put('http://localhost:5050/'+str(id), data = {'key':'value'})).json()
	elif request.form.get('accion') == 'Eliminar':
		servicios = requests.delete('http://localhost:5050/'+str(id)).json()
	return redirect("/")


if __name__ == '__main__':
    app.run(debug=True, port=5000)