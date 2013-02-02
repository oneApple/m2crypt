import EVP
from StringIO import StringIO
class TripleDES:
    def __init__(self,salt,level):
        self._salt = salt
        self._level = level
    #the length of sed is equals to the length of password
    #the sed,salt,password is must same when en/decrption
    def encryptBySha1(self,message,sed,password): 
        out=StringIO()
        m=EVP.Cipher("des_ede3_cbc", password, sed, 1, 1, "sha1", self._salt, self._level, 1) 
        out.write(m.update(message)) 
        out.write(m.final()) 
        return out.getvalue() 
    def decryptBySha1(self,message,sed,password): 
        out=StringIO()
        m=EVP.Cipher("des_ede3_cbc", password, sed, 0, 1, "sha1", self._salt, self._level, 1) 
        out.write(m.update(message)) 
        try:
            out.write(m.final())
        except:
            return None
        return out.getvalue() 
if __name__ == '__main__':
    t = TripleDES("salt",5)
    print t.decryptBySha1(t.encryptBySha1("message", "123456","passwd"),"123456" ,"passd")