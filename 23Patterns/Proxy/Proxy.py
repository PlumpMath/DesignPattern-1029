#!/usr/bin/env python
'''
Created on 2016/02/10

@author: eyotang
'''
import re, sys, os, traceback, signal

from abc import ABCMeta, abstractmethod

import time

class IGamePlayer(object):
    '''
    Abstract Game Player
    '''
    __metaclass__ = ABCMeta

    @abstractmethod
    def login(self, user, password):
        pass

    @abstractmethod
    def killBoss(self):
        pass

    @abstractmethod
    def upgrade(self):
        pass

class GamePlayer(IGamePlayer):
    '''
    Game Player Implementer
    '''
    def __init__(self, gamePlayer, name):
        if gamePlayer == None:
            raise Exception("Can't create real role!")
        self._name = name
        super(GamePlayer, self).__init__()

    def login(self, user, password):
        print "Login name: %s, user %s login successful" % (user, self._name)

    def killBoss(self):
        print "%s is killing boss..." % self._name


    def upgrade(self):
        print "%s upgrade 1 degree!" % self._name

class GamePlayerProxy(IGamePlayer):
    '''
    Game Player Proxy
    '''
    def __init__(self, name):
        self._gamePlayer = None
        try :
            self._gamePlayer = GamePlayer(self, name)
        except Exception as e :
            print "Create game player failed for name %s!" % name
            raise e
        super(GamePlayerProxy, self).__init__()

    def login(self, user, password):
        self._gamePlayer.login(user, password)

    def killBoss(self):
        self._gamePlayer.killBoss()

    def upgrade(self):
        self._gamePlayer.upgrade()



def onsignal_int(signum, frame) :
    print ("\nReceive SIGINT[Ctrl+C] to stop process by force !")
    sys.exit(-1)

def register_signal() :
    signal.signal(signal.SIGINT, onsignal_int)

def main() :
    register_signal()

    proxy = GamePlayerProxy("eyotang")
    print "start time: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    proxy.login("admin", "Admin123")
    proxy.killBoss()
    proxy.upgrade()
    print "stop time: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    return 0



if __name__ == '__main__' :
    try :
        sys.exit(main())
    except Exception as e :
        traceback.print_exc(file = sys.stderr)
        sys.exit(2)
