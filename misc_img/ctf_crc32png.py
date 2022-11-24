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


def png_crack_crc32(pngfile='ctf_crc32png.png', crack_range=4000):
    '''
    Read a png image file that can't be reading on linux platform,
    reporting Fatal error IHDR CRC error.
    Brute force crack width and height to satisfy the crc32 checksum.
    Output a cracked png file.
    '''
    f_png = open(pngfile, 'rb')
    png_bytes = f_png.read()
    f_png.close()

    data = bytearray(png_bytes[12:29])
    crc32key = int.from_bytes(png_bytes[29:33], 'big')
    for w in range(crack_range):
        for h in range(crack_range):
            data[4:8] = bytearray(struct.pack('>I', w))
            data[8:12] = bytearray(struct.pack('>I', h))
            crc32result = zlib.crc32(data)
            if crc32result == crc32key:
                print(f'cracked! weight: {w}(%s), height: {h}(%s)' % (
                    hex(w), hex(h)))
                # Output a cracked png file.
                png_cracked = bytearray(png_bytes)
                png_cracked[12:29] = data
                with open(pngfile + '_cracked.png', 'wb') as f_png_cracked:
                    f_png_cracked.write(png_cracked)
                return
    print(f'didn\'t cracked in range: {crack_range}')


def main():
    png_crack_crc32()


if __name__ == '__main__':
    main()
