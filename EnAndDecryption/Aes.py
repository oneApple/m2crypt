import BIO, RSA, EVP, util
class rsa:
    def genRsaKeypair(self,rsalen = 1024):
        rsa_key = RSA.gen_key(rsalen, 3, lambda *arg:None) 
        rsa_key.save_key("pri_key.pem", None)
        rsa_key.save_pub_key("pub_key.pem")
    def encryptionByPubkey(self,message):
        pub_key = RSA.load_pub_key("pub_key.pem")
        return pub_key.public_encrypt(message, RSA.pkcs1_padding)
    def decryptionByPrikey(self,message):
        string = open("pri_key.pem","rb").read();
        bio = BIO.MemoryBuffer(string);
        pri_key = RSA.load_key_bio(bio);
        return pri_key.private_decrypt(message,RSA.pkcs1_padding)
    def signByPrikeyAndSha1(self,message):
        m=EVP.MessageDigest("sha1") 
        m.update(message) 
        digest=m.final() 
        key_str=file("pri_key.pem","rb").read() 
        key=RSA.load_key_string(key_str, util.no_passphrase_callback) 
        return key.sign(digest, "sha1") 
    def verifyByPubkeyAndSha1(self,sign,message):
        m=EVP.MessageDigest("sha1") 
        m.update(message) 
        digest=m.final() 
        cert_str=file("pub_key.pem", "rb").read() 
        mb=BIO.MemoryBuffer(cert_str) 
        cert=RSA.load_pub_key_bio(mb)
        try:
            cert.verify(digest, sign, "sha1")
            return True
        except:
            return False

if __name__ == '__main__':
    r = rsa()
    r.genRsaKeypair()
    print r.decryptionByPrikey(r.encryptionByPubkey("message"))
    print r.verifyByPubkeyAndSha1(r.signByPrikeyAndSha1("message"), "mesage")
