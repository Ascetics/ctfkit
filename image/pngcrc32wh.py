import zlib
import struct

'''
PNG File Format in Hex:
----------------
89 50 4E 47 0D 0A 1A 0A |PNG File Header 8 bytes
00 00 00 0D             |PNG File Header block IDCH 4 bytes
49 48 44 52             |PNG File Header block IHDR 4 bytes
00 00 03 84             |PNG Image Width     4 bytes
00 00 01 7F             |PNG Image Height    4 bytes
08 06 00 00 00          |BitDepth, ColorType, CompressionMethod, FilterMethod, InterlaceMethod 5 bytes
11 84 07 C8             |CRC32Checksum 4bytes
----------------
......
----------------
00 00 00 00 49 45 4E 44 AE 42 60 82 |PNG File Tailer 12 bytes 
'''
