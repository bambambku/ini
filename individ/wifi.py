from mysecrets import *
import network, sys, time

def Wifi():
    print('Are you at home? (y/n)')
    if_home = sys.stdin.readline()
    where = ''
    if if_home == 'n\n':
        ssid = ssid_poland
        password = poland_wifi_password
    elif if_home == 'y\n':
        ssid = ssid_home
        password = home_wifi_password
    else:
        print(f'Your answer was: {if_home}')
        print('wrong answer u dafty')
        print('Wrong location')
        
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    while wlan.isconnected() == False:
        print('Waiting for connnection...')
        time.sleep(1)

    print("Connected to WIFI")
    print(wlan.ifconfig())
