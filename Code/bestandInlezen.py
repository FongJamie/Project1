import time, math
import RPi.GPIO as GPIO
# import matplotlib

# ventilator = 21
# gevraagdeTemperatuur = 28

bestandpath = "/dev/rfcomm0"

GPIO.setmode(GPIO.BCM)

def leesBestand(bestand):
    fo = open(bestand, "r")
    lijn = fo.readline()
    fo.close()
    return lijn

# def leesTemp(pLijnen):
#     positie = pLijnen[1].find("t=")
#     if positie != -1:
#         temperatuurLijn = pLijnen[1].rstrip("\n").split("t=")
#         temperatuur = float(temperatuurLijn[1])
#         return temperatuur

# try:
#     while True:
#         temperatuur = leesTemp(leesBestand(bestandpath)) /1000
#         vershilTemperatuur = temperatuur - gevraagdeTemperatuur
#
#         print("%.2f graden Celsius %f" % (temperatuur, vershilTemperatuur))
#
#         time.sleep(.5)
#
# except KeyboardInterrupt:
#     GPIO.output(ventilator, GPIO.LOW)

print(leesBestand(bestandpath))

GPIO.cleanup()
print("End program")