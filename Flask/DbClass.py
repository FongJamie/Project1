class DbClass:

    def __init__(self):
        import mysql.connector as connector

        self.__dsn = {
            "host": "localhost",
            "user": "root",
            "passwd": "!",
            "db": "project_db"
        }

        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()


    def tijdDoorsturenNaarDb(self):
        query = "INSERT INTO `project_db`.`meting`(`Tijdstip gedrukt`,`WaterbekerID`,`gebruiker_ID`) VALUES (NOW(),1,1);"
        self.__cursor.execute(query)
        self.__connection.commit()
        # self.__cursor.close()

    def ophalenTijd(self):
        query = "SELECT * FROM meting"
        self.__cursor.execute(query)
        result = self.__cursor.fetchall()
        # self.__cursor.close()
        return result

    def gebruikerAanmaken(self,naam,voornaam,geslacht,gewicht,grootte,activiteit,gebruikersnaam,wachtwoord):
        query = "INSERT INTO project_db.gebruiker(Naam,Voornaam,Geslacht,Gewicht,Grootte,Activiteit)" \
                " VALUES('"+naam+"','" +voornaam+ "','" +geslacht+ "','" + gewicht + "','" + grootte + "','" + activiteit + "')" \
                "; INSERT INTO project_db.inloggegevens(Gebruikersnaam,Wachtwoord) VALUES ('"+gebruikersnaam+"','" + wachtwoord + "') "
        self.__cursor.execute(query)
        # data committen!!
        self.__connection.commit()

    def ophalenVoornaam(self):
        query = "SELECT Voornaam FROM project_db.gebruiker"
        self.__cursor.execute(query)
        result = self.__cursor.fetchone()
        # self.__cursor.close()
        return result

    def ophalenGebruiker(self):
        query = "SELECT Voornaam,Naam, CASE gebruiker.Geslacht WHEN 0 THEN 'Man'  WHEN 1 THEN 'Vrouw' END,Gewicht,Grootte, CASE gebruiker.Activiteit WHEN 1 THEN 'Weinig'  WHEN 2 THEN 'Gemiddeld' WHEN 3 THEN 'Veel' END FROM project_db.gebruiker"
        # query = "SELECT weerstation.id, weerstation.naam, plaats.Plaats, DATE(weerstation.DatumActief), TIME(weerstation.DatumActief), CASE weerstation.Actief WHEN 0 THEN 'Neen'  WHEN 1 THEN 'Ja' END FROM db_weerstation.weerstation JOIN plaats ON weerstation.plaats_ID = plaats.ID"
        self.__cursor.execute(query)
        result = self.__cursor.fetchall()
        # self.__cursor.close()
        return result


    def gedronkenPerDag(self):
        query = "SELECT DISTINCT(date(`Tijdstip gedrukt`)),   count(id),   count(id) * (SELECT `Hoeveelheid volume` FROM waterbeker WHERE waterbeker.ID = 1) /1000 FROM project_db.meting GROUP BY date(`Tijdstip gedrukt`);"
        self.__cursor.execute(query)

        result = self.__cursor.fetchall()
        # print(result)
        return result


    def ophalenGemiddelde(self,ID):
        query = "select date(`Tijdstip gedrukt`), AVG(id) from meting WHERE gebruiker_ID = " + str(ID) + " GROUP BY DATE(`Tijdstip gedrukt`)"
        self.__cursor.execute(query)
        result = self.__cursor.fetchone()
        return result


    def instellingenWijzigen(self, nVoornaam, nNaam, nGeslacht, nGewicht, nGrootte, nActiviteit):
        query = " UPDATE project_db.gebruiker SET Voornaam = '"+nVoornaam+"', Naam = '"+nNaam+"', Geslacht = %d, Gewicht = %d, Grootte = %d, Activiteit = %d  WHERE ID = 1;" % (nGeslacht, nGewicht, nGrootte, nActiviteit)
        # print(query)
        self.__cursor.execute(query)
        self.__connection.commit()


    def wachtwoordWijzigen(self, nieuwWachtwoord):
        query = " UPDATE project_db.inloggegevens SET Wachtwoord = '"+nieuwWachtwoord+"' WHERE Gebruikersnaam = 'testGebruiker';"
        self.__cursor.execute(query)
        self.__connection.commit()

    def ophalenWachtwoord(self):
        query = "SELECT Wachtwoord FROM project_db.inloggegevens WHERE Gebruikersnaam = 'testGebruiker';"
        self.__cursor.execute(query)
        result = self.__cursor.fetchone()
        # self.__cursor.close()
        return result