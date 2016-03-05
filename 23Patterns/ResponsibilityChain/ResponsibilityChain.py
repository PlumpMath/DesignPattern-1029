#!/usr/bin/env python
'''
Created on 2016/02/10

@author: eyotang
'''
import re, sys, os, traceback, signal

from abc import ABCMeta, abstractmethod

import random

class IWoman(object):
    '''
    Abstract woman class
    '''
    __metaclass__ = ABCMeta

    @abstractmethod
    def getType(self):
        pass

    @abstractmethod
    def getRequest(self):
        pass


class Woman(IWoman):
    '''
    Woman class
    '''
    UNMARRIED, MARRIED, WIDOWED = range(3)

    def __init__(self, type, request):
        self._type = type
        if self._type == Woman.UNMARRIED:
            self._request = "Daughter's request is: " + request
        elif self._type == Woman.MARRIED:
            self._request = "Wife's request is: " + request
        elif self._type == Woman.WIDOWED:
            self._request = "Mother's request is: " + request
        else:
            self._request = "Invlid role's request is: " + request

    def getType(self):
        return self._type

    def getRequest(self):
        return self._request


class IHandler(object):
    '''
    Abstract handler class
    '''
    FATHER_LEVEL_REQ, HUSBAND_LEVEL_REQ, SON_LEVEL_REQ = range(3)
    __metaclass__ = ABCMeta
    def __init__(self, level):
        self._level = level
        self._nextHander = None

    def handleMessage(self, woman):
        if self._level == woman.getType():
            self.response(woman)
        else:
            if self._nextHander != None:
                self._nextHander.handleMessage(woman)
            else:
                print "\n------ No one can answer it, disagree! ------"

    def setNextHander(self, handler):
        self._nextHander = handler

    @abstractmethod
    def response(self, woman):
        pass

class Father(IHandler):
    '''
    Father class
    '''
    def __init__(self):
        super(Father, self).__init__(IHandler.FATHER_LEVEL_REQ)

    def response(self, woman):
        print "\n------ Daughter requests father ------"
        print woman.getRequest()
        print "Father's answer is: agree!"

class Husband(IHandler):
    '''
    Husband class
    '''
    def __init__(self):
        super(Husband, self).__init__(IHandler.HUSBAND_LEVEL_REQ)

    def response(self, woman):
        print "\n------ wife requests husband ------"
        print woman.getRequest()
        print "Husband's answer is: agree!"

class Son(IHandler):
    '''
    Son class
    '''
    def __init__(self):
        super(Son, self).__init__(IHandler.SON_LEVEL_REQ)

    def response(self, woman):
        print "\n------ Mother requests son ------"
        print woman.getRequest()
        print "Son's answer is: agree!"


def onsignal_int(signum, frame) :
    print ("\nReceive SIGINT[Ctrl+C] to stop process by force !")
    sys.exit(-1)

def register_signal() :
    signal.signal(signal.SIGINT, onsignal_int)

def main() :
    register_signal()

    womens = []
    for i in range(5):
        womens.append(Woman(random.randint(0, 4), "I wanna go shopping"))

    father = Father()
    husband = Husband()
    son = Son()

    father.setNextHander(husband)
    husband.setNextHander(son)

    for woman in womens:
        father.handleMessage(woman)


    return 0



if __name__ == '__main__' :
    try :
        sys.exit(main())
    except Exception as e :
        traceback.print_exc(file = sys.stderr)
        sys.exit(2)
