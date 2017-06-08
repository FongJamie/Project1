from Code.Model.DS1307 import DS1307
import time

test = DS1307()

# test.writeYear(17)
# test.writeMonth(6)
# test.writeDay(7)
# test.writeHours(14)
# test.writeMinutes(0)
# test.writeSeconds(0)
                                    # de MSB van register 00h staat voor "clock halt" en staat standaard op 1.
                                    # Om de klok te laten tikken zullen we daar dus een 0 moeten schrijven.


# while True:
#     print(test.read_datetime())
#     time.sleep(1)

print(test.read_datetime())