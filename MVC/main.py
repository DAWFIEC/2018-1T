import os
from flask import Flask, json, Response, render_template, request
from models import db
from models import Usuario

app = Flask(__name__)

app.config['DEBUG'] = True
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:dawespol2018@127.0.0.1:5432/postgres'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/tms'
db.init_app(app)

@app.route('/')
@app.route("/listar-usuarios")
def main():

    usuarios = Usuario.query.all()
    return render_template("index.html", usuarios=usuarios)

if __name__ == '__main__':
    app.run()