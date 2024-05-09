from keypad import KeyPad
import time
import uasyncio


class KeyPadClass():
    keyPad = KeyPad(6, 7, 8, 9, 10, 11, 12, 13)
    nokia = [['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r'],['s','t','u'],['w','x','y','z']]
    
    def __init__(self, lcd: LCD):
        self.lcd = lcd

    def key(self):
        keyvalue = self.keyPad.scan()
        if keyvalue != None:
            print(keyvalue, end="\t")
            time.sleep_ms(300)
            return keyvalue

    def enterText(self, text):
        stopEnteringText = False
        entered_string = ''
        while not stopEnteringText:
            self.lcd.display(text, 0, 0)
            entered_key = self.key()
            if entered_key:
                if entered_key == '#':
                    stopEnteringText = True
                    return entered_string
                elif entered_key == 'D':
                    if len(entered_string) > 0:
                        entered_string = entered_string[:-1]
                        self.lcd.clear()
                        self.lcd.display(text, 0, 0)
                        self.lcd.display(entered_string, 0, 1)
                else:
                    if len(entered_string) == 16:
                        continue
                    entered_string += str(entered_key)
                    self.lcd.display(entered_string, 0, 1)
                    
    def nokia3210(self, text):
        stopEnteringText = False
        entered_string = ''
        lastKey = 'G'
        index = 0
        while not stopEnteringText:
            self.lcd.display(text, 0, 0)
            entered_key = self.key()
            if entered_key:
                if entered_key == '#':
                    stopEnteringText = True
                    return entered_string
                elif entered_key == 'D':
                    if len(entered_string) > 0:
                        entered_string = entered_string[:-1]
                        self.lcd.clear()
                        self.lcd.display(text, 0, 0)
                        self.lcd.display(entered_string, 0, 1)
                elif entered_key == '*':
                    lastKey = 'G'
                elif entered_key.isdigit():
                    print(f'last key was {lastKey}')
                    if len(entered_string) == 16:
                        continue
                    if entered_key != lastKey:
                        index = 0
                        entered_string += self.nokia[int(entered_key) - 1][index]
                        lastKey = entered_key
                    if entered_key == lastKey:
                        if index == len(self.nokia[int(entered_key) - 1]) - 1:
                            index = 0
                        else:
                            index = index + 1
                        entered_string = entered_string[:-1]
                        entered_string += self.nokia[int(entered_key) - 1][index]
                    self.lcd.display(entered_string, 0, 1)
                
                    
#     async def wait_for_key(self, event, func):
#         await event.wait()
#         func()
#         
#     async def key_async(self, key, func):
#         event = uasyncio.Event()
#         task = asyncio.create_task(self.wait_for_key(event, func))
#         while True:
#             entered_key = key()
#             if entered_key == key:
#                 event.set()
#                 break
#         _ = await uasyncio.wait(task)
        
                

