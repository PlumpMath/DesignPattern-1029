#!/usr/bin/env python
'''
Created on 2016/02/29

@author: eyotang
'''
import re, sys, os, traceback, signal

from abc import ABCMeta, abstractmethod

import random

class AbstractMediator(object):
    '''
    Abstract mediator
    '''
    __metaclass__ = ABCMeta

    def __init__(self):
        self._purchase = Purchase(self)
        self._sale     = Sale(self)
        self._stock    = Stock(self)

    @abstractmethod
    def execute(self, op, args):
        pass

class Mediator(AbstractMediator):
    '''
    Mediator class
    '''
    def execute(self, op, args = None):
        if op == "purchase.buy":
            self._buyComputer(args)
        elif op == "sale.sell":
            self._sellComputer(args)
        elif op == "sale.onsale":
            self._onsale()
        elif op == "stock.clear":
            self._clearStock()

    def _buyComputer(self, num):
        saleStatus = self._sale.getSaleStatus();
        realNum = 0
        if saleStatus > 80:
            realNum = num
            print "Purchase IBM computer: %d" %realNum
        else:
            realNum = num / 2
            print "Purchase IBM computer: %d" %realNum
        self._stock.increase(realNum)

    def _sellComputer(self, num):
        if self._stock.getStockNumber() < num:
            self._stock.buyIBMComputer(num)
        self._stock.decrease(num)

    def _onsale(self):
        print "Onsale IBM computer: %d" %(self._stock.getStockNumber())

    def _clearStock(self):
        self._sale.onsale()
        self._purchase.refuseBuyIBM()


class AbstractColleague(object):
    '''
    Abstract colleague class
    '''
    __metaclass__ = ABCMeta

    def __init__(self, mediator):
        self._mediator = mediator

class Purchase(AbstractColleague):
    def __init__(self, mediator):
        super(Purchase, self).__init__(mediator)

    def buyIBMComputer(self, num):
        self._mediator.execute("purchase.buy", num)

    def refuseBuyIBM(self):
        print "Never buy IBM any more!"

class Stock(AbstractColleague):
    COMPUTER_NUMBER = 100
    def __init__(self, mediator):
        super(Stock, self).__init__(mediator)

    def increase(self, num):
        Stock.COMPUTER_NUMBER = Stock.COMPUTER_NUMBER + num
        print "Computer number in stock: %d" %Stock.COMPUTER_NUMBER

    def decrease(self, num):
        Stock.COMPUTER_NUMBER = Stock.COMPUTER_NUMBER - num
        print "Computer number in stock: %d" %Stock.COMPUTER_NUMBER

    def getStockNumber(self):
        return Stock.COMPUTER_NUMBER

    def clearStock(self):
        print "Clear computer in stock: %d" %Stock.COMPUTER_NUMBER
        self._mediator.execute("stock.clear")

class Sale(AbstractColleague):
    def __init__(self, mediator):
        super(Sale, self).__init__(mediator)

    def sellIBMComputer(self, num):
        print "Sell IBM computer: %d" %num
        self._mediator.execute("sale.sell", num)

    def getSaleStatus(self):
        saleStatus = random.randint(0, 100)
        print "Sale status of IBM computer: %d" %saleStatus
        return saleStatus

    def onsale(self):
        self._mediator.execute("sale.onsale")




def onsignal_int(signum, frame) :
    print ("\nReceive SIGINT[Ctrl+C] to stop process by force !")
    sys.exit(-1)

def register_signal() :
    signal.signal(signal.SIGINT, onsignal_int)

def main() :
    register_signal()

    mediator = Mediator()
    print "------ Purchase department buy IBM computer ------"
    purchase = Purchase(mediator)
    purchase.buyIBMComputer(100)

    print "------ Sales sell IBM computer ------"
    sale = Sale(mediator)
    sale.sellIBMComputer(1)

    print "------ Stock clear computer ------"
    stock = Stock(mediator)
    stock.clearStock()



    return 0



if __name__ == '__main__' :
    try :
        sys.exit(main())
    except Exception as e :
        traceback.print_exc(file = sys.stderr)
        sys.exit(2)
