import mysql.connector
from flask import Flask, request

app = Flask(__name__)
@app.route('/kenttä/ICAO')

def HaeKentanTiedot(icao):
    args = request.args
    sql= "select name, municipality from airport where ident = '"+icao + "'";
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount>0:
        for rivi in tulos:
            print(rivi)


yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='Kristiina',
    password='12345',
    autocommit=True
)

icao = input('Anna haluamasi kentän ICAO-koodi: ')
HaeKentanTiedot(icao)

vastaus = {
    "ICAO" : icao,
    "Name" :     ,
    "Municipality" :
}