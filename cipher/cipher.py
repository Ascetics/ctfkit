import base64
import base58
import base62
import base91
import py3base92 as base92
import hashlib


class Cipher():
    @classmethod
    def encode_string_base16(cls, s):
        s_bytes = bytes(s, encoding="utf-8")
        try:            
            return base64.b16encode(s_bytes).decode(encoding="utf-8")
        except:
            return None
    
    @classmethod
    def decode_string_base16(cls, s):
        s_bytes = bytes(s, encoding="utf-8")
        try:            
            return base64.b16decode(s_bytes).decode(encoding="utf-8")
        except:
            return None

    @classmethod
    def encode_string_base32(cls, s):
        s_bytes = bytes(s, encoding="utf-8")
        try:
            return base64.b32encode(s_bytes).decode(encoding="utf-8")
        except:
            return None

    @classmethod
    def decode_string_base32(cls, s):
        s_bytes = bytes(s, encoding="utf-8")
        try:
            return base64.b32decode(s_bytes).decode(encoding="utf-8")
        except:
            return None

    @classmethod
    def encode_string_base64(cls, s):
        s_bytes = bytes(s, encoding="utf-8")
        try:            
            return base64.b64encode(s_bytes).decode(encoding="utf-8")
        except:
            return None

    @classmethod
    def decode_string_base64(cls, s):
        s_bytes = bytes(s, encoding="utf-8")      
        try:            
            return base64.b64decode(s_bytes).decode(encoding="utf-8")
        except:
            return None

    @classmethod
    def encode_string_base85(cls, s):
        s_bytes = bytes(s, encoding="utf-8")
        try:
            return base64.b85encode(s_bytes).decode(encoding="utf-8")
        except:
            return None

    @classmethod
    def decode_string_base85(cls, s):
        s_bytes = bytes(s, encoding="utf-8")
        try:
            return base64.b85decode(s_bytes).decode(encoding="utf-8")
        except:
            return None

    @classmethod
    def encode_string_base58(cls, s):
        s_bytes = bytes(s, encoding="utf-8")
        try:            
            return base58.b58encode(s_bytes).decode(encoding="utf-8")
        except:
            return None

    @classmethod
    def decode_string_base58(cls, s):
        s_bytes = bytes(s, encoding="utf-8")      
        try:            
            return base58.b58decode(s_bytes).decode(encoding="utf-8")
        except:
            return None

    @classmethod
    def encode_string_base91(cls, s):
        s_bytes = bytearray(s, encoding="utf-8")
        try:
            return base91.encode(s_bytes)
        except:
            return None

    @classmethod
    def decode_string_base91(cls, s):
        try:
            return base91.decode(s).decode(encoding="utf-8")
        except:
            return None

    @classmethod
    def encode_string_base92(cls, s):
        try:
            return base92.encode(s)
        except:
            return None

    @classmethod
    def decode_string_base92(cls, s):
        try:
            return base92.decode(s)
        except:
            return None

    @classmethod
    def encode_string_base62(cls, s):
        s_bytes = bytes(s, encoding="utf-8")
        try:
            return base62.encodebytes(s_bytes)
        except:
            return None

    @classmethod
    def decode_string_base62(cls, s):
        try:
            return base62.decodebytes(s).decode(encoding="utf-8")
        except:
            return None

    @classmethod
    def encode_string_md5(cls, s):
        try:
            s_bytes = bytes(s, encoding="utf-8")
            md5hash = hashlib.md5(s_bytes)
            e_str = md5hash.hexdigest()
            return e_str
        except:
            return None

    @classmethod
    def decode_string_md5(cls, s):
        print("to be realized")
        pass
        
    @classmethod
    def encode_string_aes(cls, s):
        print("to be realized")
        pass

    @classmethod
    def decode_string_aes(cls, s):
        print("to be realized")
        pass

   

def test(s="Do you think the key word is welcome?"):
    result = Cipher.encode_string_base16(s)
    print("base16: %s" % result)
    result = Cipher.decode_string_base16(result)
    print("base16: %s" % result)

    result = Cipher.encode_string_base32(s)
    print("base32: %s" % result)
    result = Cipher.decode_string_base32(result)
    print("base32: %s" % result)

    result = Cipher.encode_string_base64(s)
    print("base64: %s" % result)
    result = Cipher.decode_string_base64(result)
    print("base64: %s" % result)

    result = Cipher.encode_string_base85(s)
    print("base85: %s" % result)
    result = Cipher.decode_string_base85(result)
    print("base85: %s" % result)

    result = Cipher.encode_string_base58(s)
    print("base58: %s" % result)
    result = Cipher.decode_string_base58(result)
    print("base58: %s" % result)

    result = Cipher.encode_string_base91(s)
    print("base91: %s" % result)
    result = Cipher.decode_string_base91(result)
    print("base91: %s" % result)

    result = Cipher.encode_string_base92(s)
    print("base92: %s" % result)
    result = Cipher.decode_string_base92(result)
    print("base92: %s" % result)

    result = Cipher.encode_string_base62(s)
    print("base62: %s" % result)
    result = Cipher.decode_string_base62(result)
    print("base62: %s" % result)
    
def base_family(s):
    result = Cipher.decode_string_base16(s)
    print("base16: %s" % result)
    result = Cipher.decode_string_base32(s)
    print("base32: %s" % result)
    result = Cipher.decode_string_base58(s)
    print("base58: %s" % result)
    result = Cipher.decode_string_base64(s)
    print("base64: %s" % result)
    result = Cipher.decode_string_base85(s)
    print("base85: %s" % result)
    result = Cipher.decode_string_base91(s)
    print("base91: %s" % result)
    result = Cipher.decode_string_base92(s)
    print("base92: %s" % result)
    result = Cipher.decode_string_base62(s)
    print("base62: %s" % result)

def main():
    test()
    # base_family(s="StV1DL6CwTryKyV")                        # test for base58, you should see "base58: hello world"
    # base_family(s="fPNKd")                                  # test for base91, you should see "base91: test"    
    # base_family(s="8D9Kc)=/2$WzeFui#G9Km+<{VT2u9MZil}[A")   # test for base91, you should see "base91: May a moody baby doom a yam?\n"
    # base_family(s="Jw_@V")                                    # test for base92, you should see "base92: test"
    
    # base_family(s="U2FsdGVkX1+WTSHujcCjvHj/gcwL0C7u37XtW4idGcpci3H913I=") # test for nothing

if __name__ == '__main__':
    main()
