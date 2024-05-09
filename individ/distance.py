from machine import Pin
import time

class DistanceSensor():
    Trig = Pin(19, Pin.OUT, 0)
    Echo = Pin(18, Pin.IN, 0)
    distance = 0
    soundVelocity = 340

    def getDistanceOnce(self):
        self.Trig.value(1)
        time.sleep_us(10)
        self.Trig.value(0)
        while not self.Echo.value():
            pass
        pingStart = time.ticks_us()
        while self.Echo.value():
            pass

        pingStop = time.ticks_us()
        distanceTime = time.ticks_diff(pingStop, pingStart) // 2
        self.distance = int(self.soundVelocity * distanceTime // 10000)
        return self.distance


