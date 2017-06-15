import os

from DbClass import DbClass
from flask import Flask
from flask import render_template
from flask import redirect

app = Flask(__name__)

Db_Layer = DbClass()

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
    # Dbayer.gebruikerAanmaken(name,firstname,gender,weight,height,activity,username,password)

    return render_template('registreren.html')



@app.route('/homepagina')
def homepagina():
    voornaam = Db_Layer.ophalenVoornaam()
    return render_template('homepagina.html',voornaam=voornaam[0])

@app.route('/overzicht')
def gegevens():
    gedronkenPerDag = Db_Layer.gedronkenPerDag()
    print(gedronkenPerDag)
    # datum = DB_layer.ophalenDatum()
    # print(datum)

    return render_template('gegevens.html', gedronkenPerDag=gedronkenPerDag)

@app.route('/drinklogboek')
def profiel():
    lijst_metingen = Db_Layer.ophalenTijd()
    # gebruiker = DB_layer.ophalenGebruiker()
    gebruiker = Db_Layer.ophalenGebruiker()

    return render_template('profiel.html', metingen=lijst_metingen, gebruiker=gebruiker[0])

@app.route('/instellingen', methods=['POST','GET'])
def instellingen():
    from flask import request

    if request.method == 'POST':
        voornaam = request.form['voornaam']
        naam = request.form['achternaam']
        geslacht = int(request.form['geslacht'])
        gewicht = int(request.form['gewicht'])
        grootte = int(request.form['grootte'])
        activiteit = int(request.form['activiteit'])

        # print(type(voornaam))
        # print(type(naam))
        # print(type(geslacht))
        # print(type(gewicht))
        # print(type(grootte))
        # print(type(activiteit))

        newSettings = Db_Layer.instellingenWijzigen(voornaam,naam,geslacht,gewicht,grootte,activiteit)
        return redirect ('instellingen/gegevensgewijzigd')

    return render_template('instellingen.html')



@app.route('/instellingen/gegevensgewijzigd')
def gegevensgewijzigd():
    return render_template ('gegevensgewijzigd.html')



@app.route('/instellingen/wachtwoordwijzigen', methods=['POST','GET'])
def wachtwoordwijzigen():
    from flask import request

    if request.method == 'POST':
        nieuwWachtwoord = request.form['nieuw']

        oud = request.form['oud']
        nieuw = request.form['nieuw']
        bevestig = request.form['bevestig']
        # print(type(DB_layer.ophalenWachtwoord()))
        # print(DB_layer.ophalenWachtwoord()[0])
        if (oud == Db_Layer.ophalenWachtwoord()[0]):
            if(nieuw == bevestig):
                newPassword = Db_Layer.wachtwoordWijzigen(nieuw)
                return redirect('instellingen/wachtwoordgewijzigd')


    return render_template ('wachtwoordwijzigen.html')

@app.route('/instellingen/wachtwoordgewijzigd')
def wachtwoordgewijzigd():
    return render_template('wachtwoordgewijzigd.html')


@app.route('/404')
def pageNotFound():
    return render_template('error/404.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(host='0.0.0.0', port=8080,debug=True)
