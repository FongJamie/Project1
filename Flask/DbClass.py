class DbClass:

    def __init__(self):
        import mysql.connector as connector

        self.__dsn = {
            "host": "localhost",
            "user": "root",
            "passwd": "",
            "db": "project_db"
        }

        self.__connection = connector.connect(**self.__dsn)
        self.__cursor = self.__connection.cursor()

    def getDataFromDatabase(self):
        # Query zonder parameters
        sqlQuery = "SELECT * FROM tablename"

        self.__cursor.execute(sqlQuery)
        result = self.__cursor.fetchall()
        # self.__cursor.close()
        return result

    def getDataFromDatabaseMetVoorwaarde(self, voorwaarde):
        # Query met parameters
        sqlQuery = "SELECT * FROM tablename WHERE columnname = '{param1}'"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=voorwaarde)

        self.__cursor.execute(sqlCommand)
        result = self.__cursor.fetchall()
        # self.__cursor.close()
        return result

    def setDataToDatabase(self, value1):
        # Query met parameters
        sqlQuery = "INSERT INTO tablename (columnname) VALUES ('{param1}')"
        # Combineren van de query en parameter
        sqlCommand = sqlQuery.format(param1=value1)

        self.__cursor.execute(sqlCommand)
        self.__connection.commit()
        # self.__cursor.close()

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
        query = "SELECT Voornaam,Naam,Geslacht,Gewicht,Grootte,Activiteit FROM project_db.gebruiker"
        self.__cursor.execute(query)
        result = self.__cursor.fetchall()
        # self.__cursor.close()
        return result


    def gedronkenPerDag(self, ID):
        query = "select date(`Tijdstip gedrukt`), count(id) from meting WHERE gebruiker_ID = " + str(ID) + " GROUP BY DATE(`Tijdstip gedrukt`)"
        self.__cursor.execute(query)
        result = self.__cursor.fetchone()
        # self.__cursor.close()
        return result


    def newColor(self, pCode, pName):
        try:
            query = "INSERT INTO db_weerstation.kleur " \
                    "(kleurCode, Naam) " \
                    "VALUES (%s , %s)" % (pCode, pName)
            result = self.__cursor.execute(query)
            self.__connection.commit()
            return result
        except:
            print("Error, kleur is niet toegevoegd.")
            return None
