import time

from Flask.DbClass import DbClass

db_object = DbClass()

bestandpath = "/dev/rfcomm0"


def leesBestand(bestand):
    lijn = ''
    try:
        fo = open(bestand, "r")
        lijn = fo.readline()
        lijn = lijn.rstrip('\n')
        fo.close()
    except FileNotFoundError as fnfe:
        print("Foutmelding: bestand niet gevonden.")
    return lijn

def knop_ingedrukt(karakter):
    if(karakter == "k"):
        db_object.tijdDoorsturenNaarDb()
        print("YES")


def inlezen_bestand(bestandsnaam):
    lijnen = []
    try:
        fo = open(bestandsnaam)
        lijn = fo.readline()
        while (lijn != ""):
            lijn = lijn.rstrip('\n')
            # lijn = lijn.replace("\"", "")
            try:
                # delen = lijn.split(";")
                lijnen.append(lijn)
            except:
                print("Volgende lijn werd niet verwerkt: " + lijn)

            # volgende lijn inlezen
            lijn = fo.readline()

        fo.close()

    except FileNotFoundError as fnfe:
        print("Foutmelding: bestand niet gevonden.")

    return lijnen



try:
    while True:
        var = leesBestand(bestandpath)
        # print(leesBestand(bestandpath))
        knop_ingedrukt(var)
        time.sleep(1)

except KeyboardInterrupt:
    print("Einde")

# print(inlezen_bestand(bestandpath))

# GPIO.cleanup()
# print("End program")