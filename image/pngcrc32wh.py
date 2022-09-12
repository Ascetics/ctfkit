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
    "usage: python pngcrc32wh.py -f <pngfile> -m <mode> -n <nrange>\n",
    "\tcrack a png's width or height to satisfy the crc32 checksum.\n",
    "\t<pngfile> must be a png image file.\n",
    "\t<mode> can be: width, height.\n",
    "\t<nrange> must be a valid positive integer.\n",
    "\n",))
    mode = ("width", "height")    
    argv_dict = {}

    try:
        opts, args = getopt.getopt(argv, "hf:m:n:", ["pngfile=","mode=","nrange="])
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
        elif opt in("-n", "--nrange"):
            try:
                nrange = int(arg)
                argv_dict["nrange"] = nrange
            except:
                print(usage)
                sys.exit(2)

    if argv_dict.get("pngfile") and argv_dict.get("mode") and argv_dict.get("nrange"):
        return argv_dict
    else:
        print(usage)
        sys.exit(2)

def png_crack_crc32wh(filename, mode):
    '''
    '''
    pass

def main(argv):
    argv_dict = process_cmd_argv(argv)
    pngfile, mode, nrange = argv_dict['pngfile'], argv_dict['mode'], argv_dict['nrange']
    print(pngfile, mode, nrange)

if __name__ == '__main__':
    main(sys.argv[1:])