from flask import Flask
from flask import render_template
from DbClass import DbClass
import os


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inloggen')
def inloggen():
    return render_template('inloggen.html')

@app.route('/registreren', methods=['post','get'])
def registreren():

    from flask import request

    name    = request.form['naam']
    firstname   = request.form['voornaam']
    gender = request.form['geslacht']
    weight = request.form['gewicht']
    height = request.form['grootte']
    activity = request.form['activiteit']
    username = request.form['gebruikersnaam']
    password = request.form['wachtwoord']

    # maak database object aan
    DbLayer = DbClass()
    DbLayer.gebruikerAanmaken(name,firstname,gender,weight,height,activity,username,password)

    return render_template('registreren.html')



@app.route('/homepagina')
def homepagina():
    DB_layer = DbClass()
    voornaam = DB_layer.ophalenVoornaam()
    # voornaam = firstname.rstrip('[','(','\'',',',')',']')
    return render_template('homepagina.html',voornaam=voornaam[0])

@app.route('/overzicht')
def gegevens():
    DB_layer = DbClass()
    gedronkenPerDag = DB_layer.gedronkenPerDag(1)
    return render_template('gegevens.html', gedronkenPerDag=gedronkenPerDag)

@app.route('/drinklogboek')
def profiel():
    DB_layer = DbClass()
    lijst_metingen = DB_layer.ophalenTijd()
    # gebruiker = DB_layer.ophalenGebruiker()
    gebruiker = DB_layer.ophalenGebruiker()

    return render_template('profiel.html', metingen=lijst_metingen, gebruiker=gebruiker[0])

@app.route('/instellingen')
def instellingen():
    return render_template('instellingen.html')

@app.route('/instellingen/wachtwoordwijzigen')
def wachtwoordwijzigen():
    return render_template ('wachtwoordwijzigen.html')

@app.route('/404')
def pageNotFound():
    return render_template('error/404.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0', port=80, debug=True)
