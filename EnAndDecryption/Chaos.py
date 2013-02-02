_metaclass_ = type
import random
#when u is 4,the array is chaos and random
#even two num is similar ,the array is different
#the finally result is not determined
#the initVaule is include (0,1)
class Chaos:
    def __init__(self,n):
        #create a num in [0,1)
        self._initValue = random.random()
        self._lenOfArray = n
    def calculate(self,u,x):
        return u * x * (1 - x)
    def getChaosArray(self):
        self._chaosArray = []
        x = self._initValue
        for i in range(self._lenOfArray):
            self._chaosArray.append(x)
            x = self.calculate(4.0, x)
       # print self._chaosArray
        return self._chaosArray
    def getBinaryArray(self):
        for i in range(self._lenOfArray):
            if self._chaosArray[i] > 0.5:
                self._chaosArray[i] = 1
            else:
                self._chaosArray[i] = 0
        return self._chaosArray
            
if __name__ == '__main__':
    c = Chaos(50)
    c.getChaosArray()
    print c.getBinaryArray()
    c1 = Chaos(10)
    c1.getChaosArray()
    print c1.getBinaryArray()