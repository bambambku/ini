from I2C_LCD import I2CLcd
from machine import I2C, Pin


class LCDClass():
    i2c = I2C(1, sda=Pin(14), scl=Pin(15), freq=400000)
    devices = i2c.scan()
    lcd = I2CLcd(i2c, devices[0], 2, 16)
    turned_on = False

    def display(self, text, column, row):
        try:
            self.lcd.move_to(column, row)
            self.lcd.putstr(text)
        except:
            pass
        
    def clear(self):
        self.lcd.clear()
        
    def turn_on(self):
        self.lcd.display_on()
        self.lcd.backlight_on()
        self.turned_on = True
        
    def turn_off(self):
        self.lcd.display_off()
        self.lcd.backlight_off()
        self.turned_on = False
        