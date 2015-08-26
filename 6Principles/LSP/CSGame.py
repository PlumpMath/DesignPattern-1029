#!/usr/bin/env python
'''
Created on 2015/08/15

@author: eyotang
'''
import re, sys, os, traceback, signal

class AbstractGun(object):
    '''
    Abstract Gun, can't be used
    '''
    def shoot(self):
        pass

    def shape(self):
        pass

    def sound(self):
        pass

class Handgun(AbstractGun):
    '''
    Handgun
    '''
    def __init__(self):
        super(Handgun, self).__init__()
        pass

    def shoot(self):
        print "Handgun shoot......"
        pass


class Rifle(AbstractGun):
    '''
    Rifle
    '''
    def __init__(self):
        super(Rifle, self).__init__()
        pass

    def shoot(self):
        print "Rifle shoot......"
        pass

class MachineGun(AbstractGun):
    '''
    Machine Gun
    '''
    def __init__(self):
        super(MachineGun, self).__init__()
        pass

    def shoot(self):
        print "MachineGun shoot...."
        pass

    def shape(self):
        print "MachineGun shape: |---"
        pass

    def sound(self):
        print "MachineGun sound: bia"
        pass

class AbstractToy(object):
    '''
    Abstract Toy
    '''
    def __init__(self, gun):
        self._gun = gun
        pass

    def shape(self):
        self._gun.shape()
        pass

    def sound(self):
        self._gun.sound()
        pass

    def shoot(self):
        pass

class ToyGun(AbstractToy):
    '''
    Toy Gun
    '''
    def __init__(self, gun):
        super(ToyGun, self).__init__(gun)
        pass

    def shoot(self):
        print "ToyGun shoot, for funny..."
        pass



class Soldier(object):
    '''
    Soldier to kill the enemy
    '''
    def __init__(self):
        self._gun = None
        pass

    def setGun(self, gun):
        self._gun = gun
        pass

    def killEnemy(self):
        print "Soldier start to kill the enemy......"
        self._gun.shoot()
        pass





def onsignal_int(signum, frame) :
    print ("\nReceive SIGINT[Ctrl+C] to stop process by force !")
    sys.exit(-1)

def register_signal() :
    signal.signal(signal.SIGINT, onsignal_int)

def main() :
    register_signal()

    sanMao = Soldier()
    sanMao.setGun(Rifle())
    sanMao.killEnemy()

    toyGun = ToyGun(MachineGun())
    sanMao.setGun(toyGun)
    sanMao.killEnemy()

    toyGun.shape()
    toyGun.sound()

    return 0



if __name__ == '__main__' :
    try :
        sys.exit(main())
    except Exception as e :
        traceback.print_exc(file = sys.stderr)
        sys.exit(2)
