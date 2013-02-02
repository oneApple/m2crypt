import EVP
class HashBysha1Ormd5:
    def __init__(self,alg):
        self._alg = alg
    def hash(self,message):
        m=EVP.MessageDigest(self._alg)
        m.update(message) 
        return m.digest()
if __name__ == '__main__':
    h = HashBysha1Ormd5("sha1")
    print h.hash("message")