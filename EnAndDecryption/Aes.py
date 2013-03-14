import BIO, RSA, EVP, util ,os
class rsa:
    def __init__(self,directory = "."):
        if not os.path.exists(directory):
            os.mkdir(directory)
        self.prikeyDirectory = directory + "/" + "pri_key.pem"
        self.pubkeyDirectory = directory + "/" + "pub_key.pem"
    def genRsaKeypair(self,rsalen = 1024):
        rsa_key = RSA.gen_key(rsalen, 3, lambda *arg:None) 
        
        rsa_key.save_key(self.prikeyDirectory, None)
        rsa_key.save_pub_key(self.pubkeyDirectory)
    def encryptionByPubkey(self,message):
        pub_key = RSA.load_pub_key(self.pubkeyDirectory)
        return pub_key.public_encrypt(message, RSA.pkcs1_padding)
    def decryptionByPrikey(self,message):
        string = open(self.prikeyDirectory,"rb").read();
        bio = BIO.MemoryBuffer(string);
        pri_key = RSA.load_key_bio(bio);
        return pri_key.private_decrypt(message,RSA.pkcs1_padding)
    def signByPrikeyAndSha1(self,message):
        m=EVP.MessageDigest("sha1") 
        m.update(message) 
        digest=m.final() 
        key_str=file(self.prikeyDirectory,"rb").read() 
        key=RSA.load_key_string(key_str, util.no_passphrase_callback) 
        return key.sign(digest, "sha1") 
    def verifyByPubkeyAndSha1(self,sign,message):
        m=EVP.MessageDigest("sha1") 
        m.update(message) 
        digest=m.final() 
        cert_str=file(self.pubkeyDirectory, "rb").read() 
        mb=BIO.MemoryBuffer(cert_str) 
        cert=RSA.load_pub_key_bio(mb)
        try:
            cert.verify(digest, sign, "sha1")
            return True
        except:
            return False

if __name__ == '__main__':
    r = rsa("../key")
    r.genRsaKeypair()
    print r.decryptionByPrikey(r.encryptionByPubkey("message"))
    print r.verifyByPubkeyAndSha1(r.signByPrikeyAndSha1("message"), "message")
