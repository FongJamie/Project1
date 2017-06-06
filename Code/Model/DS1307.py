import smbus
from datetime import datetime


class DS1307():
    _ADDRESS_SECONDS = 0x00
    _ADDRESS_MINUTES = 0x01
    _ADDRESS_HOURS = 0x02
    _ADDRESS_DAY = 0x03
    _ADDRESS_DATE = 0x04
    _ADDRESS_MONTH = 0x05
    _ADDRESS_YEAR = 0x06
    _ADDRESS_CONTROL = 0x07

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
        return self.__BCDtoInt(self.__read(self._ADDRESS_YEAR))

    def writeYear(self, jaartal):
        return self.__write(self._ADDRESS_YEAR, self.__IntToBCD(jaartal))

    #Month
    def getMonth(self):
        return self.__BCDtoInt(self.__read(self._ADDRESS_MONTH))

    def writeMonth(self, maand):
        return self.__write(self._ADDRESS_MONTH, self.__IntToBCD(maand))

    #Day
    def getDay(self):
        return self.__BCDtoInt(self.__read(self._ADDRESS_DAY))

    def writeDay(self, dag):
        return self.__write(self._ADDRESS_DAY, self.__IntToBCD(dag))

    #Hours
    def getHours(self):
        return self.__BCDtoInt(self.__read(self._ADDRESS_HOURS))

    def writeHours(self, uur):
        return self.__write(self._ADDRESS_HOURS, self.__IntToBCD(uur))

    #Minutes
    def getMinutes(self):
        return self.__BCDtoInt(self.__read(self._ADDRESS_MINUTES))

    def writeMinutes(self, minuten):
        return self.__write(self._ADDRESS_MINUTES, self.__IntToBCD(minuten))

    #Seconden
    def getSeconds(self):
        return self.__BCDtoInt(self.__read(self._ADDRESS_SECONDS))

    def writeSeconds(self, seconden):
        return self.__write(self._ADDRESS_SECONDS, self.__IntToBCD(seconden))




    def read_datetime(self, century=21):
        return datetime((century - 1) * 100 + self.getYear(),
                        self.getMonth(), self.getDay() , self.getHours(), self.getMinutes(), self.getSeconds())

