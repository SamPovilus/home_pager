#! /usr/bin/env python3
import sys
from gpiozero import RGBLED, Button
from time import sleep
from threading import Thread
    
class HomePager():
    led1 = RGBLED(red=22,green=27,blue=17,active_high = False)
    alertB = Button(21,bounce_time=0.02)
    alarmB = Button(16,bounce_time=0.02)
    alerting = False
    alarming = False
    is_main_console = False
    def main(self):
        if(sys.argv[1] == "main"):
            print("Am main console")
        else:
            print("Am remote console")
        print(sys.argv[1])
        self.params = HomePager.Params()
        print(self.params.MAIN_CONSOLE_SEND_PORT)
        self.alertB.when_pressed = self.alert_pressed
        self.alarmB.when_pressed = self.alarm_pressed

        self.foo = HomePager.Remote(self)
        self.foo.mainLoop()
        
    def alert_pressed(self):
        self.alerting = True

    def alarm_pressed(self):
        self.alarming = True

    class Params():
        """ A class to hold the parameters for the home pager """
        MAIN_CONSOLE_RECEVE_PORT = 32323
        MAIN_CONSOLE_SEND_PORT   = 32324

    class Remote():
        """ This will be the thing running on the remotes. Because I bought toggle switches instead of momentaries I think I will just look for \delta 's in the switches, I may go ahead and by some momentaries, but for now this will work. The remote will send out a message once a second  and listen for an acknowlage from the central base station. All other remotes will silently receive the packet and replicate the state of the remote. The central box will receive the state and then send out an acknowlage. When the remote receves an acknowlage from the central box, they will stop blinking and store state."""
        def __init__(self,parent):
            self.parent = parent
        
        def mainLoop(self):
            while True:
                print("Alerting %s Alarming %s" % (self.parent.alerting, self.parent.alarming))
                sleep(0.1)
                    
                
                
if __name__== "__main__":
  hp = HomePager()
  hp.main()



