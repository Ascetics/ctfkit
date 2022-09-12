import os
import sys
import getopt
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

def process_cmd_argv(argv):
    usage = "".join((
    "\n",
    "usage: python pngcrc32wh.py -h\n",
    "\techo this help message.\n",
    "usage: python pngcrc32wh.py -f <pngfile> -m <mode> -n <crack_range>\n",
    "\tcrack a png's width or height to satisfy the crc32 checksum.\n",
    "\t<pngfile> must be a png image file.\n",
    "\t<mode> can be: width, height.\n",
    "\t<crack_range> must be a valid positive integer.\n",
    "\n",))
    mode = ("width", "height")    
    argv_dict = {}

    try:
        opts, args = getopt.getopt(argv, "hf:m:n:", ["pngfile=","mode=","crack_range="])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            sys.exit()
        elif opt in ("-f", "--pngfile"):
            argv_dict["pngfile"] = arg
        elif opt in ("-m", "--mode") and arg in mode:
            argv_dict["mode"] = arg
        elif opt in("-n", "--crack_range"):
            try:
                crack_range = int(arg)
                argv_dict["crack_range"] = crack_range
            except:
                print(usage)
                sys.exit(2)

    if argv_dict.get("pngfile") and argv_dict.get("mode") and argv_dict.get("crack_range"):
        return argv_dict
    else:
        print(usage)
        sys.exit(2)

def png_crack_crc32wh(pngfile, mode, crack_range):
    '''
    Read a png image file that can't be reading on linux platform, 
    reporting Fatal error IHDR CRC error.
    Brute force crack width or height to satisfy the crc32 checksum.
    Output a cracked png file.
    '''
    with open(pngfile, "rb") as fin:
        png_bytes = fin.read()
        if "width" == mode:
            wh_offset = 4
        elif "height" == mode:
            wh_offset = 8

        # Brute force crack width or height to satisfy the crc32 checksum.
        # Bytes can't be read or witten. You must use a bytearray.
        data = bytearray(png_bytes[12:29])
        crc32key = int.from_bytes(png_bytes[29:33], "big")
        for n in range(crack_range):
            substitute = bytearray(struct.pack(">I", n))
            for i in range(4):
                data[wh_offset+i] = substitute[i]
            crc32result = zlib.crc32(data)
            if crc32result == crc32key:
                print("crack %s : " % mode, hex(n))

                # Output a cracked png file.
                png_bytearray = bytearray(png_bytes)
                png_bytearray[12:29] = data
                with open(pngfile+"_new.png", "wb") as fout:
                    fout.write(png_bytearray)
                break

        


def main(argv):
    argv_dict = process_cmd_argv(argv)
    pngfile, mode, crack_range = argv_dict.get("pngfile"), argv_dict.get("mode"), argv_dict.get("crack_range")
    png_crack_crc32wh(pngfile, mode, crack_range)

if __name__ == '__main__':
    main(sys.argv[1:])