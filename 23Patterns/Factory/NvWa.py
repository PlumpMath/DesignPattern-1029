#!/usr/bin/env python
'''
Created on 2015/08/15

@author: eyotang
'''
import re, sys, os, traceback, signal

from abc import ABCMeta, abstractmethod

class Human(object):
    '''
    Basic class human
    '''
    __metaclass__ = ABCMeta

    @abstractmethod
    def getColor(self):
        pass

    @abstractmethod
    def speak(self):
        pass

class BlackHuman(Human):
    '''
    Black human
    '''
    def __init__(self):
        super(BlackHuman, self).__init__()
        pass

    def getColor(self):
        print "The color of BlackHuman is Black!"
        pass

    def speak(self):
        print "BlackHuman can speak, but no one can understand it."
        pass

class YellowHuman(Human):
    '''
    Yellow human
    '''
    def __init__(self):
        super(YellowHuman, self).__init__()
        pass

    def getColor(self):
        print "The color of YellowHuman is Yellow!"
        pass

    def speak(self):
        print "YellowHuman can speak, normally DWORD."
        pass

class WhiteHuman(Human):
    '''
    White human
    '''
    def __init__(self):
        super(WhiteHuman, self).__init__()
        pass

    def getColor(self):
        print "The color of WhiteHuman is White!"
        pass

    def speak(self):
        print "WhiteHuman can speak, normally single byte."
        pass


class AbstractHumanFactory(object):
    '''
    Abstract Human Factory
    '''

    __metaclass__ = ABCMeta

    @abstractmethod
    def createHuman(self, C):
        pass

class HumanFactory(AbstractHumanFactory):
    '''
    Human Factory
    '''
    def __init__(self):
        super(HumanFactory, self).__init__()
        pass

    def createHuman(self, C):
        try:
            human = C()
        except Exception as e:
            raise Exception("Human create error!" + str(e))

        return human


def onsignal_int(signum, frame) :
    print ("\nReceive SIGINT[Ctrl+C] to stop process by force !")
    sys.exit(-1)

def register_signal() :
    signal.signal(signal.SIGINT, onsignal_int)

def main() :
    register_signal()

    yinYangLu = HumanFactory()

    print "\n--First group is white human--"
    human = yinYangLu.createHuman(WhiteHuman)
    human.getColor()
    human.speak()

    print "\n--Second group is black human--"
    human = yinYangLu.createHuman(BlackHuman)
    human.getColor()
    human.speak()

    print "\n--Third group is yellow human--"
    human = yinYangLu.createHuman(YellowHuman)
    human.getColor()
    human.speak()

    return 0



if __name__ == '__main__' :
    try :
        sys.exit(main())
    except Exception as e :
        traceback.print_exc(file = sys.stderr)
        sys.exit(2)
