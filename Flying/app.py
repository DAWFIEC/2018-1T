from flask import Flask, json, Response, request, render_template
from pymongo import MongoClient # Database connector
from bson.objectid import ObjectId # For ObjectId to work

#client = MongoClient('localhost', 27017)    #Configure the connection to the database
client = MongoClient('mongodb://aavendan:624mlbclassi@ds135747.mlab.com:35747/flying',35747)
db = client.flying    #Select the database
routes = db.routes #Select the collection

app = Flask(__name__)

@app.route('/')
def index():
	origenes=db.routes.distinct("sAirport")
	destinos=db.routes.distinct("dAirport")

	return render_template('formulario.html',origenes=origenes, destinos=destinos)

@app.route('/find', methods = ['POST'])
def find():
	if request.method == 'POST':
		origenes=db.routes.distinct("sAirport")
		destinos=db.routes.distinct("dAirport")
		
		origen = request.form["origen"]
		destino = request.form["destino"]
		stops = int(request.form["tipo"])
		print(request.form)

		size = db.routes.find({"sAirport":origen, "dAirport":destino, "stops":stops}).count()

		if(size > 0):

			rutas = db.routes.aggregate([
				{"$match": {'sAirport':origen,'dAirport':destino}},
				{"$lookup":{"from":"airlines","localField":"airlineID","foreignField":"airlineID","as":"extra"}
				}])


			return render_template('resultados.html',origenes=origenes, destinos=destinos,rutas=rutas)

		return render_template('vacio.html',origenes=origenes, destinos=destinos)

	

if __name__ == '__main__':
    app.run(debug=True, port=5000)