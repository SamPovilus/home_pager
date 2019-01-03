#! /usr/bin/env python3
import sys
from gpiozero import RGBLED, Button
from time import sleep
from threading import Thread
    
class HomePager(object):
    led1 = RGBLED(red=22,green=27,blue=17,active_high = False)
    alertB = Button(21,bounce_time=0.02)
    alarmB = Button(16,bounce_time=0.02)
    alerting = False
    alarming = False
    is_main_console = False
    def main():
        if(sys.argv[1] == "main"):
            print("Am main console")
        else:
            print("am remote console")
        print(sys.argv[1])
        print(Params.MAIN_CONSOLE_SEND_PORT)
        alertB.when_pressed = alert_pressed
        alarmB.when_pressed = alarm_pressed

        foo = Remote()
        foo.mainLoop
        
        def alert_pressed():
            alerting = True

        def alarm_pressed():
            alarming = True

        class Params(object):
            """ A class to hold the parameters for the home pager """
            MAIN_CONSOLE_RECEVE_PORT = 32323
            MAIN_CONSOLE_SEND_PORT   = 32324

        class Remote(object):
            """ This will be the thing running on the remotes. Because I bought toggle switches instead of momentaries I think I will just look for \delta 's in the switches, I may go ahead and by some momentaries, but for now this will work. The remote will send out a message once a second  and listen for an acknowlage from the central base station. All other remotes will silently receive the packet and replicate the state of the remote. The central box will receive the state and then send out an acknowlage. When the remote receves an acknowlage from the central box, they will stop blinking and store state."""
            def mainLoop():
                while True:
                    print("Alerting %s Alarming %s" % (alerting, alarming))
                    
                
                
if __name__== "__main__":
  HomePager.main()



