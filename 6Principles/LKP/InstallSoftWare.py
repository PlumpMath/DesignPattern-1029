#!/usr/bin/env python
'''
Created on 2015/08/15

@author: eyotang
'''
import re, sys, os, traceback, signal

import random

class Wizard(object):
    '''
    Wizard
    '''
    def __first(self):
        print "execute 1st method..."
        return random.randint(0, 100)

    def __second(self):
        print "execute 2nd method..."
        return random.randint(0, 100)

    def __third(self):
        print "execute 3rd method..."
        return random.randint(0, 100)

    def installWizard(self):
        result = self.__first()
        if (result > 50):
            result = self.__second()
            if (result > 50):
                result = self.__third()

class InstallSoftware(object):
    '''
    Install the software
    '''
    def installWizard(self, wizard):
        wizard.installWizard()
        pass



def onsignal_int(signum, frame) :
    print ("\nReceive SIGINT[Ctrl+C] to stop process by force !")
    sys.exit(-1)

def register_signal() :
    signal.signal(signal.SIGINT, onsignal_int)

def main() :
    register_signal()

    invoker = InstallSoftware()
    invoker.installWizard(Wizard())

    return 0



if __name__ == '__main__' :
    try :
        sys.exit(main())
    except Exception as e :
        traceback.print_exc(file = sys.stderr)
        sys.exit(2)
