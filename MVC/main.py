import os
from flask import Flask, json, Response, render_template, request
from models import db
from models import Usuario

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:dawespol2018@127.0.0.1:5432/postgres'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres+psycopg2://axvwlocqwtmici:acff0eee633d876448574ce5ae5c2b3da08399311802efa6dd89ede5a930c18f@ec2-54-235-240-126.compute-1.amazonaws.com:5432/d31v7km2jaubs4'
db.init_app(app)

@app.route('/')
@app.route("/listar-usuarios")
def main():

    usuarios = Usuario.query.all()
    return render_template("index.html", usuarios=usuarios)

if __name__ == '__main__':
    app.run()