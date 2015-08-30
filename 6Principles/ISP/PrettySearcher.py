#!/usr/bin/env python
'''
Created on 2015/08/15

@author: eyotang
'''
import re, sys, os, traceback, signal

from abc import ABCMeta, abstractmethod



class IGreatTemperamentGirl(object):
    '''
    Interface of great temperament girl
    '''
    def __init__(self, name):
        self._name = name
        pass

    def greatTemperament(self):
        print "%s---temperament is great" % self._name
        pass

class IGoodBodyGirl():
    '''
    Interface of good body girl
    '''
    def __init__(self, name):
        self._name = name
        pass

    def goodLooking(self):
        print "%s---face is beautiful" % self._name
        pass

    def niceFigure(self):
        print "%s---figure is very nice" % self._name
        pass

class PrettyGirl(IGreatTemperamentGirl, IGoodBodyGirl):
    '''
    Implement of pretty girl
    '''
    def __init__(self, name):
        super(PrettyGirl, self).__init__(name)
        pass


class AbstractSearcher(object):
    '''
    Abstract searcher
    '''
    __metaclass__ = ABCMeta

    def __init__(self, prettyGirl):
        self._prettyGirl = prettyGirl
        pass

    @abstractmethod
    def show(self):
        pass

class Searcher(AbstractSearcher):
    '''
    Searcher
    '''
    def __init__(self, prettyGirl):
        super(Searcher, self).__init__(prettyGirl)
        pass

    def show(self):
        self._prettyGirl.goodLooking()
        self._prettyGirl.niceFigure()
        self._prettyGirl.greatTemperament()
        pass




def onsignal_int(signum, frame) :
    print ("\nReceive SIGINT[Ctrl+C] to stop process by force !")
    sys.exit(-1)

def register_signal() :
    signal.signal(signal.SIGINT, onsignal_int)

def main() :
    register_signal()

    yanYan = PrettyGirl("Yanyan")
    searcher = Searcher(yanYan)
    searcher.show()

    return 0



if __name__ == '__main__' :
    try :
        sys.exit(main())
    except Exception as e :
        traceback.print_exc(file = sys.stderr)
        sys.exit(2)
