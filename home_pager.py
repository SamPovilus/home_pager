#! /usr/bin/env python3
import sys

class Params(object):
    """ A class to hold the parameters for the home pager """
    MAIN_CONSOLE_RECEVE_PORT = 32323
    MAIN_CONSOLE_SEND_PORT   = 32324
    
class HomePager(object):
    is_main_console = False
    def main():
        if(sys.argv[1] == "main"):
            print("Am main console")
        else:
            print("am remote console")
        print(sys.argv[1])
        print(Params.MAIN_CONSOLE_SEND_PORT)
  
if __name__== "__main__":
  HomePager.main()



