#!/usr/bin/env python
'''
Created on 2016/02/10

@author: eyotang
'''
import re, sys, os, traceback, signal

from abc import ABCMeta, abstractmethod

class Group(object):
    '''
    Abstract group class
    '''
    __metaclass__ = ABCMeta

    @abstractmethod
    def find(self):
        pass

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def change(self):
        pass

    @abstractmethod
    def plan(self):
        pass


class CodeGroup(Group):
    '''
    Code group
    '''
    def find(self):
        print "find code group"

    def add(self):
        print "Customer required to add one function..."

    def delete(self):
        print "Customer required to delete one function..."

    def change(self):
        print "Customer required to change one function..."

    def plan(self):
        print "Customer request code change plan..."

class PageGroup(Group):
    '''
    Page group class
    '''

    def find(self):
        print "find page group"

    def add(self):
        print "Customer required to add one page..."

    def delete(self):
        print "Customer required to delete one page..."

    def change(self):
        print "Customer required to change one page..."

    def plan(self):
        print "Customer request page change plan..."


class RequirementGroup(Group):
    '''
    Requirement group class
    '''

    def find(self):
        print "find requirement group"

    def add(self):
        print "Customer required to add one requirement..."

    def delete(self):
        print "Customer required to delete one requirement..."

    def change(self):
        print "Customer required to change one requirement..."

    def plan(self):
        print "Customer request requirement change plan..."


class Command(object):
    '''
    Abstract command class
    '''
    __metaclass__ = ABCMeta

    def __init__(self):
        self._rg = RequirementGroup()
        self._pg = PageGroup()
        self._cg = CodeGroup()

    @abstractmethod
    def execute(self):
        pass


class AddRequirementCommand(Command):
    '''
    Add requirement command
    '''
    def __init__(self):
        super(AddRequirementCommand, self).__init__()

    def execute(self):
        self._rg.find()
        self._rg.add()
        self._rg.plan()

class DeletePageCommand(Command):
    '''
    Delete page command
    '''
    def __init__(self):
        super(DeletePageCommand, self).__init__()

    def execute(self):
        self._pg.find()
        self._pg.delete()
        self._pg.plan()


class Invoker(object):
    '''
    Invoker class
    '''
    def __init__(self):
        self._command = None

    def setCommand(self, cmd):
        self._command = cmd

    def action(self):
        self._command.execute()



def onsignal_int(signum, frame) :
    print ("\nReceive SIGINT[Ctrl+C] to stop process by force !")
    sys.exit(-1)

def register_signal() :
    signal.signal(signal.SIGINT, onsignal_int)

def main() :
    register_signal()

    addRequirementCmd = AddRequirementCommand()
    deletePageCmd     = DeletePageCommand()
    xiaoSan = Invoker()

    print "\n------ Customer required to add new requirement ------"
    xiaoSan.setCommand(addRequirementCmd)
    xiaoSan.action()

    print "\n------ Customer required to delete one page ------"
    xiaoSan.setCommand(deletePageCmd)
    xiaoSan.action()

    return 0



if __name__ == '__main__' :
    try :
        sys.exit(main())
    except Exception as e :
        traceback.print_exc(file = sys.stderr)
        sys.exit(2)
