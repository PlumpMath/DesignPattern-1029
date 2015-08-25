#!/usr/bin/env python
'''
Created on 2015/08/15

@author: eyotang
'''
import re, sys, os, traceback, signal


class UserBO(object):
    '''
    User properties
    '''
    def __init__(self):
        self._userId   = None
        self._password = None
        self._userName = None

        pass

    @property
    def userId(self):
        return self._userId
    @userId.setter
    def userId(self, value):
        self._userId = value

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, value):
        self._password = value

    @property
    def userName(self):
        return self._userName
    @userName.setter
    def userName(self, value):
        self._userName = value


class UserBiz(object):
    '''
    User behaviors
    '''
    def __init__(self):
        self._userList = []
        pass

    def changePassword(self, userBO, value):
        print "start to change password!"
        userBO.password = value

    def deleteUser(self, userBO):
        if userBO in self._userList:
            print "delete user success: id:%s, name:%s" %(userBO.userId, userBO.userName)
        else:
            print "delete user failed, not found"


class UserInfo(UserBiz):
    '''
    User Information
    '''

    def __init__(self):
        super(UserInfo, self).__init__()
        pass

    def createUser(self, userId, userName, password):
        user = UserBO()
        user.userId = userId
        user.userName = userName
        user.password = password

        self._userList.append(user)
        return user


def onsignal_int(signum, frame) :
    print ("\nReceive SIGINT[Ctrl+C] to stop process by force !")
    sys.exit(-1)

def register_signal() :
    signal.signal(signal.SIGINT, onsignal_int)

def main() :
    register_signal()

    userInfo = UserInfo()
    user = userInfo.createUser(1234, "eyotang", "123456")

    userInfo.changePassword(user, "abcd1234")
    userInfo.deleteUser(user)

    user = UserBO()
    userInfo.deleteUser(user)

    return 0



if __name__ == '__main__' :
    try :
        sys.exit(main())
    except Exception as e :
        traceback.print_exc(file = sys.stderr)
        sys.exit(2)
