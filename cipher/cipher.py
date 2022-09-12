import base64
import base58
import hashlib


class Cipher():
    @classmethod
    def encode_string_base16(cls, s):
        s_bytes = bytes(s, encoding="utf-8")
        try:            
            e_bytes = base64.b16encode(s_bytes)
            e_str = str(e_bytes, encoding="utf-8")
            return e_str
        except:
            return None
    
    @classmethod
    def decode_string_base16(cls, s):
        s_bytes = bytes(s, encoding="utf-8")
        try:            
            d_bytes = base64.b16decode(s_bytes)
            d_str = str(d_bytes, encoding="utf-8")
            return d_str
        except:
            return None

    @classmethod
    def encode_string_base32(cls, s):
        s_bytes = bytes(s, encoding="utf-8")
        try:
            e_bytes = base64.b32encode(s_bytes)
            e_str = str(e_bytes, encoding="utf-8")
            return e_str
        except:
            return None

    @classmethod
    def decode_string_base32(cls, s):
        s_bytes = bytes(s, encoding="utf-8")
        try:
            d_bytes = base64.b32decode(s_bytes)
            d_str = str(d_bytes, encoding="utf-8")
            return d_str
        except:
            return None

    @classmethod
    def encode_string_base64(cls, s):
        s_bytes = bytes(s, encoding="utf-8")
        try:            
            e_bytes = base64.b64encode(s_bytes)
            e_str = str(e_bytes, encoding="utf-8")
            return e_str
        except:
            return None

    @classmethod
    def decode_string_base64(cls, s):
        s_bytes = bytes(s, encoding="utf-8")      
        try:            
            d_bytes = base64.b64decode(s_bytes)
            d_str = str(d_bytes, encoding="utf-8")
            return d_str
        except:
            return None

    @classmethod
    def encode_string_base58(cls, s):
        s_bytes = bytes(s, encoding="utf-8")
        try:            
            e_bytes = base58.b58encode(s_bytes)
            e_str = str(e_bytes, encoding="utf-8")
            return e_str
        except:
            return None

    @classmethod
    def decode_string_base58(cls, s):
        s_bytes = bytes(s, encoding="utf-8")      
        try:            
            d_bytes = base58.b58decode(s_bytes)
            d_str = str(d_bytes, encoding="utf-8")
            return d_str
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

    @classmethod
    def encode_string_base85(cls, s):
        s_bytes = bytes(s, encoding="utf-8")
        try:
            e_bytes = base64.b85encode(s_bytes)
            e_str = str(e_bytes, encoding="utf-8")
            return e_str
        except:
            return None

    @classmethod
    def decode_string_base85(cls, s):
        s_bytes = bytes(s, encoding="utf-8")
        try:
            d_bytes = base64.b85decode(s_bytes)
            d_str = str(d_bytes, encoding="utf-8")
            return d_str
        except:
            return None

def test(s="Do you think the key word is welcome?"):
    result = Cipher.encode_string_base16(s)
    print("base16: %s" % result)
    result = Cipher.decode_string_base16(result)
    print("base16: %s" % result)

    result = Cipher.encode_string_base32(s)
    print("base32: %s" % result)
    result = Cipher.decode_string_base32(result)
    print("base32: %s" % result)

    result = Cipher.encode_string_base58(s)
    print("base58: %s" % result)
    result = Cipher.decode_string_base58(result)
    print("base58: %s" % result)

    result = Cipher.encode_string_base64(s)
    print("base64: %s" % result)
    result = Cipher.decode_string_base64(result)
    print("base64: %s" % result)

    result = Cipher.encode_string_base85(s)
    print("base85: %s" % result)
    result = Cipher.decode_string_base85(result)
    print("base85: %s" % result)
    
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
    pass

def main():
    test()
    base_family(s="U2FsdGVkX1+WTSHujcCjvHj/gcwL0C7u37XtW4idGcpci3H913I=")

if __name__ == '__main__':
    main()
