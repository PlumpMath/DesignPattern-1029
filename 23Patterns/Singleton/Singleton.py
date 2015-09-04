#!/usr/bin/env python
'''
Created on 2015/08/15

@author: eyotang
'''
import re, sys, os, traceback, signal


class Singleton(type):
    '''
    Meta class of sigleton
    '''
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls._instance = None

    def __call__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__call__(*args, **kw)
        return cls._instance

class Emperor(object):
    '''
    Emperor singleton
    '''
    __metaclass__ = Singleton

    def getInstance(self):
        return self._instance

    def say(self):
        print "I'm the emperor"




def onsignal_int(signum, frame) :
    print ("\nReceive SIGINT[Ctrl+C] to stop process by force !")
    sys.exit(-1)

def register_signal() :
    signal.signal(signal.SIGINT, onsignal_int)

def main() :
    register_signal()

    instance = Emperor().getInstance()
    instance.say()

    print id(instance)
    print id(Emperor())

    return 0



if __name__ == '__main__' :
    try :
        sys.exit(main())
    except Exception as e :
        traceback.print_exc(file = sys.stderr)
        sys.exit(2)
