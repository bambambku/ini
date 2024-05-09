from machine import Pin

class MotionSensor():
    sensorPin = Pin(17, Pin.IN, Pin.PULL_UP)
    
    
    def detectOnce(self):
        if self.sensorPin.value() != 0:
            return 1
        else:
            return 0
        



