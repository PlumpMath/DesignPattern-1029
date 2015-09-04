#!/usr/bin/env python
'''
Created on 2015/08/15

@author: eyotang
'''
import re, sys, os, traceback, signal

from abc import ABCMeta, abstractmethod

class IBook(object):
    '''
    Abstract book
    '''
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, name, price, author):
        self._name = name
        self._price = price
        self._author = author
        pass

    def getName(self):
        return self._name

    def getPrice(self):
        return self._price

    def getAuthor(self):
        return self._author

class NovelBook(IBook):
    '''
    Novel book
    '''
    def __init__(self, name, price, author):
        super(NovelBook, self).__init__(name, price, author)
        pass

class OffNovelBook(NovelBook):
    '''
    Off Novel Book
    '''
    def __init__(self, name, price, author):
        super(OffNovelBook, self).__init__(name, price, author)
        pass

    def getPrice(self):
        offPrice = 0
        if (self._price > 4000):
            offPrice = self._price * 90 / 100
        else:
            offPrice = self._price * 80 / 100

        return offPrice

class IComputerBook(IBook):
    '''
    Abstract class IComputerBook
    '''
    def __init__(self, name, price, author, scope):
        super(IComputerBook, self).__init__(name, price, author)
        self._scope = scope
        pass

    def getScope(self):
        return self._scope

class ComputerBook(IComputerBook):
    '''
    Implement of ComputerBook
    '''
    def __init__(self, name, price, author, scope):
        super(ComputerBook, self).__init__(name, price, author, scope)
        pass


class BookStore(object):
    '''
    Book store
    '''
    bookList = []
    bookList.append(NovelBook("Wei Chen", 4000, "Qian Zhongshu"))
    bookList.append(OffNovelBook("Dragon Oath", 3200, "JinYong"))
    bookList.append(OffNovelBook("Notre Dame de Paris", 5600, "Hugo"))
    bookList.append(OffNovelBook("The Golden Lotus", 4300, "Lanling Xiaoxiao Sheng"))
    bookList.append(ComputerBook("Think in Java", 4300, "Bruce Eckel", "Program Language"))

    def __init__(self):
        pass

    @classmethod
    def getBookList(cls):
        return cls.bookList


def onsignal_int(signum, frame) :
    print ("\nReceive SIGINT[Ctrl+C] to stop process by force !")
    sys.exit(-1)

def register_signal() :
    signal.signal(signal.SIGINT, onsignal_int)

def main() :
    register_signal()

    print "----------------------------------------------------------------------"
    print "           Books sold from the book store as following:"
    print "----------------------------------------------------------------------"
    for book in BookStore.getBookList():
        print "Book Name:%s" % book.getName()
        print "Author   :%s" % book.getAuthor()
        print "Price    :%.2f RMB" % (book.getPrice()/100.0)

    return 0



if __name__ == '__main__' :
    try :
        sys.exit(main())
    except Exception as e :
        traceback.print_exc(file = sys.stderr)
        sys.exit(2)
