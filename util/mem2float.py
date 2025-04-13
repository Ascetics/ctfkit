import struct
"""
内存值是0x408E147B
转换成float数是4.440000057220459
"""
hex_value = 0x408E147B
float_value = struct.unpack('!f', struct.pack('!I', hex_value))[0]
print(float_value)
