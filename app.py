# python.exe -m venv .venv
# cd .venv/Scripts
# activate.bat
# py -m ensurepip --upgrade
# pip install -r requirements.txt

from flask import Flask

from flask import render_template
from flask import request
from flask import jsonify, make_response

import mysql.connector

import datetime
import pytz

from flask_cors import CORS, cross_origin

con = mysql.connector.connect(
    host="82.197.82.90",
    database="u861594054_practica4_Dand",
    user="u861594054_Dandi_pr4",
    password="#Zorrilla21#"
)

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    if not con.is_connected():
        con.reconnect()

    con.close()

    return render_template("index.html")

@app.route("/app")
def app2():
    if not con.is_connected():
        con.reconnect()

    con.close()

    return "<h5> estoy en un html con angular instalado en flask mamá✔</h5>"

@app.route("/ahorros")
def ahorros():
    if not con.is_connected():
        con.reconnect()

    cursor = con.cursor(dictionary=True)
    sql    = """SELECT movimientosetiquetas.IdMovimientoEtiqueta,
             movimientos.monto, movimientos.fechaHora, etiquetas.nombreEtiqueta 
               FROM movimientosetiquetas 
               INNER JOIN movimientos ON movimientos.idMovimiento = movimientosetiquetas.idMovimiento 
               INNER JOIN etiquetas ON etiquetas.idEtiqueta = movimientosetiquetas.idEtiqueta 
               LIMIT 10
    """

    cursor.execute(sql)
    registros = cursor.fetchall()
    return render_template("ahorros.html", ahorros=registros)

@app.route("/etiquetas")
def etiquetas():
    if not con.is_connected():
        con.reconnect()

    cursor = con.cursor(dictionary=True)
    sql    = """SELECT * FROM etiquetas"""

    cursor.execute(sql)
    registros = cursor.fetchall()



    return render_template("etiquetas.html", etiquetas=registros)

@app.route("/movimientos")
def movimientos():
    if not con.is_connected():
        con.reconnect()

    cursor = con.cursor(dictionary=True)

    sql = """SELECT * FROM movimientos """  
    
    cursor.execute(sql)
    registros = cursor.fetchall()

    return render_template("movimientos.html", movs=registros)
