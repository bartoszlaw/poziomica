# pip3 install smbus2 in terminal
from smbus2 import SMBus

class i2cConnector():
    """Klasa zawiera zestaw metod wykorzystywanych do obsługi podstawowej komunikacji za pomocą protokołu I2C"""

    def __init__(self):
        self.bus = SMBus(1)
    
    def readByte(adress, offset):
        """ Odczytuje jeden bajt danych z podanego adresu """
        return self.bus.read_byte_data(adress, offset)
        
    
    def readBlock(adress, offset, size):
        """ Odczytuje blok danych z adresu (powyżej jednego bajtu) """
        return self.bus.read_i2c_block_data(adress, offset, adress)
       
    
    def writeByte(adress, offset, data):
        """ Zapisuje wartość zmiennej `data` do podanego adresu. 'data' =< 1 bajt """
        return self.bus.write_byte_data(adress, offset, data)
    
    def writeBlock(adress, offset, data):
        """ Zapisuje blok danych do podanego adresu. 'Data' > 1 bajt """
        return self.bus.write_i2c_block_data(adress, 0, data)  