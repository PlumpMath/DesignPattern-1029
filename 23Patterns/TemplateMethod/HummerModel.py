#!/usr/bin/env python
'''
Created on 2015/08/15

@author: eyotang
'''

import re, sys, os, traceback, signal

from abc import ABCMeta, abstractmethod

class HummerModel(object):
    '''
    Abstact class HummerModel
    '''
    __metaclass__ = ABCMeta

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def alarm(self):
        pass

    @abstractmethod
    def engineBoom(self):
        pass

    def isAlarm(self):
        return True

    def run(self):
        self.start()
        self.engineBoom()
        if self.isAlarm():
            self.alarm()
        self.stop()

class HummerH1Model(HummerModel):
    '''
    Hummer H1 Model
    '''
    def __init__(self):
        super(HummerH1Model, self).__init__()
        self._isAlarm = True

    def start(self):
        print "Hummer H1 start..."

    def alarm(self):
        print "Hummer H1 bell..."

    def stop(self):
        print "Hummer H1 stop..."

    def engineBoom(self):
        print "Hummer H1 engine bomm..."

    def setAlarm(self, isAlarm):
        self._isAlarm = isAlarm

    def isAlarm(self):
        return self._isAlarm

class HummerH2Model(HummerModel):
    '''
    Hummer H2 Model
    '''
    def __init__(self):
        super(HummerH2Model, self).__init__()

    def start(self):
        print "Hummer H2 start..."

    def alarm(self):
        print "Hummer H2 bell..."

    def stop(self):
        print "Hummer H2 stop..."

    def engineBoom(self):
        print "Hummer H2 engine bomm..."

    def isAlarm(self):
        return False

def onsignal_int(signum, frame) :
    print ("\nReceive SIGINT[Ctrl+C] to stop process by force !")
    sys.exit(-1)

def register_signal() :
    signal.signal(signal.SIGINT, onsignal_int)

def main() :
    register_signal()

    print "------- Hummer H1 Model -------"
    hummer = HummerH1Model()
    prompt = "Hummer H1 require bell or not? [Y/n] "
    text = raw_input(prompt)
    input = text.strip().upper()[0]
    if input == 'Y':
        hummer.setAlarm(True)
    else:
        hummer.setAlarm(False)
    hummer.run()

    print "------- Hummer H2 Model -------"
    hummer = HummerH2Model()
    hummer.run()

    return 0



if __name__ == '__main__' :
    try :
        sys.exit(main())
    except Exception as e :
        traceback.print_exc(file = sys.stderr)
        sys.exit(2)
