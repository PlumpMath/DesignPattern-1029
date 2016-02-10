#!/usr/bin/env python
'''
Created on 2016/02/10

@author: eyotang
'''
import re, sys, os, traceback, signal

from abc import ABCMeta, abstractmethod

class CarModel(object):
    '''
    Abstact class CarModel
    '''
    __metaclass__ = ABCMeta
    def __init__(self):
        self._sequence = []

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

    def run(self):
        for actionName in self._sequence:
            if actionName == "start":
                self.start()
            elif actionName == "alarm":
                self.alarm()
            elif actionName == "stop":
                self.stop()
            elif actionName == "engine boom":
                self.engineBoom()

    def setSequence(self, sequence):
        self._sequence = sequence

class BenzModel(CarModel):
    '''
    Benz Model
    '''
    def __init__(self):
        super(BenzModel, self).__init__()

    def start(self):
        print "Benz start..."

    def alarm(self):
        print "Benz bell..."

    def stop(self):
        print "Benz stop..."

    def engineBoom(self):
        print "Benz engine bomm..."

class BMWModel(CarModel):
    '''
    BMW Model
    '''
    def __init__(self):
        super(BMWModel, self).__init__()

    def start(self):
        print "BMW start..."

    def alarm(self):
        print "BMW bell..."

    def stop(self):
        print "BMW stop..."

    def engineBoom(self):
        print "BMW engine bomm..."


class CarBuilder(object):
    '''
    Abstract car builder
    '''
    __metaclass__ = ABCMeta

    @abstractmethod
    def setSequence(self, sequence):
        pass

    @abstractmethod
    def getCarModel(self):
        pass

class BenzBuilder(CarBuilder):
    '''
    Benz car builder
    '''
    def __init__(self):
        super(BenzBuilder, self).__init__()
        self._benz = BenzModel()

    def getCarModel(self):
        return self._benz

    def setSequence(self, sequence):
        self._benz.setSequence(sequence)

class BMWBuilder(CarBuilder):
    '''
    BMW car builder
    '''
    def __init__(self):
        super(BMWBuilder, self).__init__()
        self._bmw = BMWModel()

    def getCarModel(self):
        return self._bmw

    def setSequence(self, sequence):
        self._bmw.setSequence(sequence)

class Director(object):
    '''
    Director class, control builder
    '''
    def __init__(self):
        self._benzBuilder = BenzBuilder()
        self._bmwBuilder = BMWBuilder()

    def getABenzModel(self):
        self._benzBuilder.setSequence(["start", "stop"])
        return self._benzBuilder.getCarModel()

    def getBBenzModel(self):
        self._benzBuilder.setSequence(["engine boom","start", "stop"])
        return self._benzBuilder.getCarModel()

    def getCBMWModel(self):
        self._bmwBuilder.setSequence(["alarm","start", "stop"])
        return self._bmwBuilder.getCarModel()

    def getDBMWModel(self):
        self._bmwBuilder.setSequence(["start"])
        return self._bmwBuilder.getCarModel()


def onsignal_int(signum, frame) :
    print ("\nReceive SIGINT[Ctrl+C] to stop process by force !")
    sys.exit(-1)

def register_signal() :
    signal.signal(signal.SIGINT, onsignal_int)

def main() :
    register_signal()

    director = Director()
    print "------- A Benz Model -------"
    for i in range(10):
        director.getABenzModel().run()

    print "------- B Benz Model -------"
    for i in range(100):
        director.getBBenzModel().run()

    print "------- C BMW Model -------"
    for i in range(20):
        director.getCBMWModel().run()

    print "------- D BMW Model -------"
    for i in range(200):
        director.getDBMWModel().run()

    return 0



if __name__ == '__main__' :
    try :
        sys.exit(main())
    except Exception as e :
        traceback.print_exc(file = sys.stderr)
        sys.exit(2)
