from random import getrandbits

_g = 2
_bits = 32

class diffieHellman:
    def __init__(self):
        self.__prime = 29989
        self.__randnum = getrandbits(_bits)
        self.pubkey = pow(_g, self.__randnum, self.__prime)
    def getPubkey(self):
        return self.pubkey
    def getKey(self,otherpubkey):
        return pow(otherpubkey,self.__randnum, self.__prime)
    
if __name__ == '__main__':
    d1 = diffieHellman()
    d2 = diffieHellman()
    print d1.getPubkey()
    print d2.getPubkey()
    print d2.getKey(d1.getPubkey())
    print d1.getKey(d2.getPubkey())
    