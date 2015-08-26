#!/usr/bin/env python
'''
Created on 2015/08/15

@author: eyotang
'''
import re, sys, os, traceback, signal

class ICar(object):
    '''
    Abstract car
    '''
    def __init__(self):
        self._name = None
        pass

    def run(self):
        print "%s start to run..." % self._name
        pass


class Benz(ICar):
    '''
    Benz Car
    '''
    def __init__(self):
        super(Benz, self).__init__()
        self._name = "Benz"
        pass

class BMW(ICar):
    '''
    BMW car
    '''
    def __init__(self):
        super(BMW, self).__init__()
        self._name = "BMW"
        pass


class IDriver(object):
    '''
    Abstract Driver
    '''
    def __init__(self, car):
        self._car = car
        pass

    def setCar(self, car):
        self._car = car
        pass

    def drive(self):
        pass

class Driver(IDriver):
    '''
    Driver, will drive the car
    '''
    def __init__(self):
        super(Driver, self).__init__(ICar())
        pass

    def drive(self):
        self._car.run()
        pass



def onsignal_int(signum, frame) :
    print ("\nReceive SIGINT[Ctrl+C] to stop process by force !")
    sys.exit(-1)

def register_signal() :
    signal.signal(signal.SIGINT, onsignal_int)

def main() :
    register_signal()

    benz = Benz()
    bmw  = BMW()
    zhangSan = Driver()

    zhangSan.setCar(benz)
    zhangSan.drive()

    zhangSan.setCar(bmw)
    zhangSan.drive()

    return 0



if __name__ == '__main__' :
    try :
        sys.exit(main())
    except Exception as e :
        traceback.print_exc(file = sys.stderr)
        sys.exit(2)
