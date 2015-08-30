#!/usr/bin/env python
'''
Created on 2015/08/15

@author: eyotang
'''
import re, sys, os, traceback, signal


class Girl(object):
    '''
    Girl
    '''
    def __init__(self):
        pass

class GroupLeader(object):
    '''
    Group leader, counter grils
    '''
    def __init__(self, girlList):
        self._girlList = girlList
        pass

    def countGirls(self):
        print "Number of girls:%s" % len(self._girlList)
        pass

class Teacher(object):
    '''
    Teacher
    '''
    def command(self, groupLeader):
        groupLeader.countGirls()
        pass


def onsignal_int(signum, frame) :
    print ("\nReceive SIGINT[Ctrl+C] to stop process by force !")
    sys.exit(-1)

def register_signal() :
    signal.signal(signal.SIGINT, onsignal_int)

def main() :
    register_signal()

    girlList = []
    for i in range(20):
        girlList.append(Girl())

    teacher = Teacher()
    teacher.command(GroupLeader(girlList))

    return 0



if __name__ == '__main__' :
    try :
        sys.exit(main())
    except Exception as e :
        traceback.print_exc(file = sys.stderr)
        sys.exit(2)
