from machine import Pin, SoftSPI
from mfrc522 import MFRC522
import time

class RFIDClass():
    sck = Pin(2, Pin.OUT)
    copi = Pin(3, Pin.OUT) # Controller out, peripheral in
    cipo = Pin(4, Pin.OUT) # Controller in, peripheral out

    def __init__(self):
        self.spi = SoftSPI(baudrate=100000, polarity=0, phase=0, sck=self.sck, mosi=self.copi, miso=self.cipo)
        self.sda = Pin(5, Pin.OUT)
        self.reader = MFRC522(self.spi, self.sda)

    def scan(self):
            (status, tag_type) = self.reader.request(self.reader.CARD_REQIDL)#Read the card type number
            if status == self.reader.OK:
                (status, raw_uid) = self.reader.anticoll()#Reads the card serial number of the selected card
                if status == self.reader.OK:
                    tag = f'{raw_uid[0]}{raw_uid[1]}{raw_uid[2]}{raw_uid[3]}'
                    return tag
    def scanTag(self):
        tagScanned = False
        while tagScanned == False:
            tag = self.scan()
            if tag:
                tagScanned = True
            time.sleep_ms(20)
        return tag

