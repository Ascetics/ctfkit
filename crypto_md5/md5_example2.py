from hashlib import md5

PRINTABLES = b"!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
PRINTABLES_SUB = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_@"


def text_to_md5hash(text):
    m = md5()
    m.update(text)
    md5hash = m.hexdigest()
    return md5hash


def build_text(text, index):
    if index < len(text):
        for ch in PRINTABLES_SUB:
            text[index] = ch
            build_text(text, index + 1)
    else:
        md5hash = text_to_md5hash(text)
        print(text.decode('utf-8'), md5hash)


def construct_text(text_len=1):
    text = bytearray(text_len)
    build_text(text, index=0)


if __name__ == '__main__':
    construct_text(1)
    construct_text(2)
