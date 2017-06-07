import smbus
from datetime import datetime


class DS1307():
    _addressSeconds = 0x00
    _addressMinutes = 0x01
    _addressHours = 0x02
    _addressDay = 0x03
    _addressDate = 0x04
    _addressMonth = 0x05
    _addressYear = 0x06
    _addressControl = 0x07

    def __init__(self, i2cbus=1, address=0x68):  # 7 bits + R/W toevoegen
        self.bus = smbus.SMBus(1)  # pi 1 => bus 0 vanaf pi2 => bus 1
        self.address = address

    def __BCDtoInt(self, data):
        e = data & 0x0f
        t = data >> 4
        return 10 * t + e


    def __IntToBCD(self, number):
        e = number % 10
        t = number // 10
        return t << 4 | e   #OR


    def __read(self, register):
        return self.bus.read_byte_data(self.address, register)

    def __write(self, register, data):
        return self.bus.write_byte_data(self.address, register, data)



    #Year
    def getYear(self):
        return self.__BCDtoInt(self.__read(self._addressYear))

    def writeYear(self, jaartal):
        return self.__write(self._addressYear, self.__IntToBCD(jaartal))

    #Month
    def getMonth(self):
        return self.__BCDtoInt(self.__read(self._addressMonth))

    def writeMonth(self, maand):
        return self.__write(self._addressMonth, self.__IntToBCD(maand))

    #Day
    def getDay(self):
        return self.__BCDtoInt(self.__read(self._addressDay))

    def writeDay(self, dag):
        return self.__write(self._addressDay, self.__IntToBCD(dag))

    #Hours
    def getHours(self):
        return self.__BCDtoInt(self.__read(self._addressHours))

    def writeHours(self, uur):
        return self.__write(self._addressHours, self.__IntToBCD(uur))

    #Minutes
    def getMinutes(self):
        return self.__BCDtoInt(self.__read(self._addressMinutes))

    def writeMinutes(self, minuten):
        return self.__write(self._addressMinutes, self.__IntToBCD(minuten))

    #Seconden
    def getSeconds(self):
        return self.__BCDtoInt(self.__read(self._addressSeconds))

    def writeSeconds(self, seconden):
        return self.__write(self._addressSeconds, self.__IntToBCD(seconden))



    #Volledige datum lezen
    def read_datetime(self, century=21):
        return datetime((century - 1) * 100 + self.getYear(),
                        self.getMonth(), self.getDay() , self.getHours(), self.getMinutes(), self.getSeconds())

