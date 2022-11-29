import base64
import base58
import base62
import base91
import py3base92 as base92
import base36
import hashlib


class Cipher():
    @staticmethod
    def enc_base16(s_bytes):
        try:
            return base64.b16encode(s_bytes)
        except:
            return None

    @staticmethod
    def dec_base16(s_bytes):
        try:
            return base64.b16decode(s_bytes)
        except:
            return None

    @staticmethod
    def enc_base32(s_bytes):
        try:
            return base64.b32encode(s_bytes)
        except:
            return None

    @staticmethod
    def dec_base32(s_bytes):
        try:
            return base64.b32decode(s_bytes)
        except:
            return None

    @staticmethod
    def enc_base64(s_bytes):
        try:
            return base64.b64encode(s_bytes)
        except:
            return None

    @staticmethod
    def dec_base64(s_bytes):
        try:
            return base64.b64decode(s_bytes)
        except:
            return None

    @staticmethod
    def enc_base85(s_bytes):
        try:
            return base64.b85encode(s_bytes)
        except:
            return None

    @staticmethod
    def dec_base85(s_bytes):
        try:
            return base64.b85decode(s_bytes)
        except:
            return None

    @staticmethod
    def enc_base58(s_bytes):
        try:
            return base58.b58encode(s_bytes)
        except:
            return None

    @staticmethod
    def dec_base58(s_bytes):
        try:
            return base58.b58decode(s_bytes)
        except:
            return None

    @staticmethod
    def enc_base91(s_bytes):
        try:
            return base91.encode(s_bytes)
        except:
            return None

    @staticmethod
    def dec_base91(s_bytes):
        try:
            return base91.decode(s_bytes)
        except:
            return None

    @staticmethod
    def enc_base92(s_bytes):
        try:
            return base92.encode(s_bytes)
        except:
            return None

    @staticmethod
    def dec_base92(s_bytes):
        try:
            return base92.decode(s_bytes)
        except:
            return None

    @staticmethod
    def enc_base62(s_bytes):
        try:
            return base62.encodebytes(s_bytes)
        except:
            return None

    @staticmethod
    def dec_base62(s_bytes):
        try:
            return base62.decodebytes(s_bytes)
        except:
            return None

    @staticmethod
    def dec_base36(s):
        '''
        bin, oct, dec, hex, base36.
        base36 require a string and return an integer.
        '''
        try:
            return base36.loads(s)
        except:
            return None

    @staticmethod
    def encode_string_md5(s):
        try:
            s_bytes = bytes(s, encoding="utf-8")
            md5hash = hashlib.md5(s_bytes)
            e_str = md5hash.hexdigest()
            return e_str
        except:
            return None


def base_family(s="Do you think the key word is welcome?"):
    s = s.encode('utf-8')
    result = Cipher.enc_base16(s)
    print("base16: %s" % result)
    result = Cipher.dec_base16(result)
    print("base16: %s" % result)

    result = Cipher.enc_base32(s)
    print("base32: %s" % result)
    result = Cipher.dec_base32(result)
    print("base32: %s" % result)

    result = Cipher.enc_base64(s)
    print("base64: %s" % result)
    result = Cipher.dec_base64(result)
    print("base64: %s" % result)

    result = Cipher.enc_base85(s)
    print("base85: %s" % result)
    result = Cipher.dec_base85(result)
    print("base85: %s" % result)

    result = Cipher.enc_base58(s)
    print("base58: %s" % result)
    result = Cipher.dec_base58(result)
    print("base58: %s" % result)

    result = Cipher.enc_base91(s)
    print("base91: %s" % result)
    result = Cipher.dec_base91(result)
    print("base91: %s" % result)

    result = Cipher.enc_base92(s)
    print("base92: %s" % result)
    result = Cipher.dec_base92(result)
    print("base92: %s" % result)

    result = Cipher.enc_base62(s)
    print("base62: %s" % result)
    result = Cipher.dec_base62(result)
    print("base62: %s" % result)




def main():
    base_family()
    # base_family(s="StV1DL6CwTryKyV")                        # test for base58, you should see "base58: hello world"
    # base_family(s="fPNKd")                                  # test for base91, you should see "base91: test"    
    # base_family(s="8D9Kc)=/2$WzeFui#G9Km+<{VT2u9MZil}[A")   # test for base91, you should see "base91: May a moody baby doom a yam?\n"
    # base_family(s="Jw_@V")                                  # test for base92, you should see "base92: test"

    # base_family(s="U2FsdGVkX1+WTSHujcCjvHj/gcwL0C7u37XtW4idGcpci3H913I=") # test for nothing


if __name__ == '__main__':
    main()
