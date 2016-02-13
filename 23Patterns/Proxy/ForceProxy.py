#!/usr/bin/env python
'''
Created on 2016/02/13

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

    @abstractmethod
    def getProxy(self):
        pass

class GamePlayer(IGamePlayer):
    '''
    Game Player Implementer
    '''
    def __init__(self, name):
        self._name = name
        self._proxy = None
        super(GamePlayer, self).__init__()

    def login(self, user, password):
        if self._isProxy():
            print "Login name: %s, user %s login successful" % (user, self._name)
        else:
            print "please use specific proxy!"

    def killBoss(self):
        if self._isProxy():
            print "%s is killing boss..." % self._name
        else:
            print "please use specific proxy!"

    def upgrade(self):
        if self._isProxy():
            print "%s upgrade 1 degree!" % self._name
        else:
            print "please use specific proxy!"

    def getProxy(self):
        self._proxy = GamePlayerProxy(self)
        return self._proxy

    def _isProxy(self):
        if self._proxy != None:
            return True
        else:
            return False

class GamePlayerProxy(IGamePlayer):
    '''
    Game Player Proxy
    '''
    def __init__(self, gamePlayer):
        self._gamePlayer = gamePlayer
        super(GamePlayerProxy, self).__init__()

    def login(self, user, password):
        self._gamePlayer.login(user, password)

    def killBoss(self):
        self._gamePlayer.killBoss()

    def upgrade(self):
        self._gamePlayer.upgrade()

    def getProxy(self):
        return self



def onsignal_int(signum, frame) :
    print ("\nReceive SIGINT[Ctrl+C] to stop process by force !")
    sys.exit(-1)

def register_signal() :
    signal.signal(signal.SIGINT, onsignal_int)

def main() :
    register_signal()

    player = GamePlayer("eyotang")
    print "start time: " + time.strftime("%Y-%m-%d %H:%M:%S ==>", time.localtime())
    player.login("admin", "Admin123")
    player.killBoss()
    player.upgrade()
    print "stop time: " + time.strftime("%Y-%m-%d %H:%M:%S  <==", time.localtime())

    player = GamePlayer("eyotang")
    proxy = GamePlayerProxy(player)
    print "start time: " + time.strftime("%Y-%m-%d %H:%M:%S ==>", time.localtime())
    proxy.login("admin", "Admin123")
    proxy.killBoss()
    proxy.upgrade()
    print "stop time: " + time.strftime("%Y-%m-%d %H:%M:%S  <==", time.localtime())

    proxy = GamePlayer("eyotang").getProxy()
    print "start time: " + time.strftime("%Y-%m-%d %H:%M:%S ==>", time.localtime())
    proxy.login("admin", "Admin123")
    proxy.killBoss()
    proxy.upgrade()
    print "stop time: " + time.strftime("%Y-%m-%d %H:%M:%S  <==", time.localtime())

    return 0



if __name__ == '__main__' :
    try :
        sys.exit(main())
    except Exception as e :
        traceback.print_exc(file = sys.stderr)
        sys.exit(2)
