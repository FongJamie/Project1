from Code.Model.DS1307 import DS1307
import time

test = DS1307()

# print(test.writeYear(17))
# print(test.writeMonth(05))
# print(test.writeDay(03))
# print(test.writeHours(10))
# print(test.writeMinutes(22))
# print(test.writeSeconds(0))
                                    # de MSB van register 00h staat voor "clock halt" en staat standaard op 1.
                                    # Om de klok te laten tikken zullen we daar dus een 0 moeten schrijven.


while True:
    print(test.read_datetime())
    time.sleep(1)
