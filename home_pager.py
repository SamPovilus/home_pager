#! /usr/bin/env python3
import sys
from gpiozero import RGBLED, Button
from time import sleep

    
class HomePager(object):
    led1 = RGBLED(red=22,green=27,blue=17,active_high = False)
    switch = Button(23,pull_up=False,bounce_time=0.02)
    is_main_console = False
    def main():
        if(sys.argv[1] == "main"):
            print("Am main console")
        else:
            print("am remote console")
        print(sys.argv[1])
        print(Params.MAIN_CONSOLE_SEND_PORT)

        class Params(object):
            """ A class to hold the parameters for the home pager """
            MAIN_CONSOLE_RECEVE_PORT = 32323
            MAIN_CONSOLE_SEND_PORT   = 32324

if __name__== "__main__":
  HomePager.main()



