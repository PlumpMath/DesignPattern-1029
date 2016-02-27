#!/usr/bin/env python
'''
Created on 2016/02/27

@author: eyotang
'''
import re, sys, os, traceback, signal

from abc import ABCMeta, abstractmethod

import string, random, copy

def getRandString(num):
    ret = "".join(random.choice(string.ascii_letters) for x in range(num))
    return ret

def sendMail(mail):
    print "Title: " + mail.getSubject() + "\tReceiver: " + mail.getReceiver() + "\t...send successfully!"

class AdvTemplate(object):
    '''
    Advertisement template
    '''
    def __init__(self):
        self._advSubject = "XX Bank draw lottery activity"
        self._advContext = "Notice: Give you 1,000,000 RMB, if you use the credit card."

    def getAdvSubject(self):
        return self._advSubject

    def getAdvContext(self):
        return self._advContext

class Mail(object):
    '''
    Mail class
    '''
    def __init__(self, advTemplate):
        self._receiver    = ""
        self._subject     = advTemplate.getAdvSubject()
        self._appellation = ""
        self._context     = advTemplate.getAdvContext()
        self._tail        = ""

    def clone(self):
        return copy.deepcopy(self)

    def getReceiver(self):
        return self._receiver

    def setReceiver(self, receiver):
        self._receiver = receiver

    def getSubject(self):
        return self._subject

    def setSubject(self, subject):
        self._subject = subject

    def getAppellation(self):
        return self._appellation

    def setAppellation(self, appellation):
        self._appellation = appellation

    def getContext(self):
        return self._context

    def setContext(self, context):
        self._context = context

    def getTail(self):
        return self._tail

    def setTail(self, tail):
        self._tail = tail


def onsignal_int(signum, frame) :
    print ("\nReceive SIGINT[Ctrl+C] to stop process by force !")
    sys.exit(-1)

def register_signal() :
    signal.signal(signal.SIGINT, onsignal_int)

def main() :
    register_signal()

    MAX_COUNT = 6
    mail = Mail(AdvTemplate())
    mail.setTail("XXX Bank copyright")
    for i in range(MAX_COUNT):
        cloneMail = mail.clone()
        cloneMail.setAppellation(getRandString(5) + "Gentlemen(Lady)")
        cloneMail.setReceiver(getRandString(5) + "@" + getRandString(8) + ".com")
        sendMail(cloneMail)

    return 0



if __name__ == '__main__' :
    try :
        sys.exit(main())
    except Exception as e :
        traceback.print_exc(file = sys.stderr)
        sys.exit(2)
