import os
import sys
import getopt
import matplotlib.pyplot as plt
import numpy as np

USAGE = "".join((
    "\n",
    "USAGE: python usb.py -f <pcapfile> -m <mode>",
    "\n",
    "\t<mode> can be: move, left, right, both or all.\n",
    "\trepresent move mouse, left btn down, right btn down, both button down.\n",
    "all represent move && left && right && both\n",
    "\n",
    "DEPENDENCY(wireshark): tshark\n",
    "DEPENDENCY(python package): numpy & matplotlib\n",))

MOUSE_LOCUS = {
    'all': {
        'x': [0],
        'y': [0],
        'colors': ['grey']
    },
    'move': {
        'x': [0],
        'y': [0],
        'color': 'grey',
    },
    'left': {
        'x': [0],
        'y': [0],
        'color': 'blue',
    },
    'right': {
        'x': [0],
        'y': [0],
        'color': 'red',
    },
    'both': {
        'x': [0],
        'y': [0],
        'color': 'purple',
    },
}

KEYBOARD_MAP = {
    # a-z upper A-Z
    0x04: {"desc": "Keyboard_a", "symbol": "a", "ascii": 0x61, "upper_symbol": "A", "upper_ascii": 0x41, },
    0x05: {"desc": "Keyboard_b", "symbol": "b", "ascii": 0x62, "upper_symbol": "B", "upper_ascii": 0x42, },
    0x06: {"desc": "Keyboard_c", "symbol": "c", "ascii": 0x63, "upper_symbol": "C", "upper_ascii": 0x43, },
    0x07: {"desc": "Keyboard_d", "symbol": "d", "ascii": 0x64, "upper_symbol": "D", "upper_ascii": 0x44, },
    0x08: {"desc": "Keyboard_e", "symbol": "e", "ascii": 0x65, "upper_symbol": "E", "upper_ascii": 0x45, },
    0x09: {"desc": "Keyboard_f", "symbol": "f", "ascii": 0x66, "upper_symbol": "F", "upper_ascii": 0x46, },
    0x0A: {"desc": "Keyboard_g", "symbol": "g", "ascii": 0x67, "upper_symbol": "G", "upper_ascii": 0x47, },
    0x0B: {"desc": "Keyboard_h", "symbol": "h", "ascii": 0x68, "upper_symbol": "H", "upper_ascii": 0x48, },
    0x0C: {"desc": "Keyboard_i", "symbol": "i", "ascii": 0x69, "upper_symbol": "I", "upper_ascii": 0x49, },
    0x0D: {"desc": "Keyboard_j", "symbol": "j", "ascii": 0x6A, "upper_symbol": "J", "upper_ascii": 0x4A, },
    0x0E: {"desc": "Keyboard_k", "symbol": "k", "ascii": 0x6B, "upper_symbol": "K", "upper_ascii": 0x4B, },
    0x0F: {"desc": "Keyboard_l", "symbol": "l", "ascii": 0x6C, "upper_symbol": "L", "upper_ascii": 0x4C, },
    0x10: {"desc": "Keyboard_m", "symbol": "m", "ascii": 0x6D, "upper_symbol": "M", "upper_ascii": 0x4D, },
    0x11: {"desc": "Keyboard_n", "symbol": "n", "ascii": 0x6E, "upper_symbol": "N", "upper_ascii": 0x4E, },
    0x12: {"desc": "Keyboard_o", "symbol": "o", "ascii": 0x6F, "upper_symbol": "O", "upper_ascii": 0x4F, },
    0x13: {"desc": "Keyboard_p", "symbol": "p", "ascii": 0x70, "upper_symbol": "P", "upper_ascii": 0x50, },
    0x14: {"desc": "Keyboard_q", "symbol": "q", "ascii": 0x71, "upper_symbol": "Q", "upper_ascii": 0x51, },
    0x15: {"desc": "Keyboard_r", "symbol": "r", "ascii": 0x72, "upper_symbol": "R", "upper_ascii": 0x52, },
    0x16: {"desc": "Keyboard_s", "symbol": "s", "ascii": 0x73, "upper_symbol": "S", "upper_ascii": 0x53, },
    0x17: {"desc": "Keyboard_t", "symbol": "t", "ascii": 0x74, "upper_symbol": "T", "upper_ascii": 0x54, },
    0x18: {"desc": "Keyboard_u", "symbol": "u", "ascii": 0x75, "upper_symbol": "U", "upper_ascii": 0x55, },
    0x19: {"desc": "Keyboard_v", "symbol": "v", "ascii": 0x76, "upper_symbol": "V", "upper_ascii": 0x56, },
    0x1A: {"desc": "Keyboard_w", "symbol": "w", "ascii": 0x77, "upper_symbol": "W", "upper_ascii": 0x57, },
    0x1B: {"desc": "Keyboard_x", "symbol": "x", "ascii": 0x78, "upper_symbol": "X", "upper_ascii": 0x58, },
    0x1C: {"desc": "Keyboard_y", "symbol": "y", "ascii": 0x79, "upper_symbol": "Y", "upper_ascii": 0x59, },
    0x1D: {"desc": "Keyboard_z", "symbol": "z", "ascii": 0x7A, "upper_symbol": "Z", "upper_ascii": 0x5A, },

    # 0-9 upper !@#$%^&*()
    0x1E: {"desc": "Keyboard_1", "symbol": "1", "ascii": 0x31, "upper_symbol": "!", "upper_ascii": 0x21, },
    0x1F: {"desc": "Keyboard_2", "symbol": "2", "ascii": 0x32, "upper_symbol": "@", "upper_ascii": 0x40, },
    0x20: {"desc": "Keyboard_3", "symbol": "3", "ascii": 0x33, "upper_symbol": "#", "upper_ascii": 0x23, },
    0x21: {"desc": "Keyboard_4", "symbol": "4", "ascii": 0x34, "upper_symbol": "$", "upper_ascii": 0x24, },
    0x22: {"desc": "Keyboard_5", "symbol": "5", "ascii": 0x35, "upper_symbol": "%", "upper_ascii": 0x25, },
    0x23: {"desc": "Keyboard_6", "symbol": "6", "ascii": 0x36, "upper_symbol": "^", "upper_ascii": 0x5E, },
    0x24: {"desc": "Keyboard_7", "symbol": "7", "ascii": 0x37, "upper_symbol": "&", "upper_ascii": 0x26, },
    0x25: {"desc": "Keyboard_8", "symbol": "8", "ascii": 0x38, "upper_symbol": "*", "upper_ascii": 0x2A, },
    0x26: {"desc": "Keyboard_9", "symbol": "9", "ascii": 0x39, "upper_symbol": "(", "upper_ascii": 0x28, },
    0x27: {"desc": "Keyboard_0", "symbol": "0", "ascii": 0x30, "upper_symbol": ")", "upper_ascii": 0x29, },

    # other keyboard key
    0x28: {"desc": "Keyboard_Enter", "symbol": "<Enter>", "ascii": 0x0D, },
    0x29: {"desc": "Keyboard_Escape", "symbol": "<ESC>", "ascii": 0x1B, },
    0x2A: {"desc": "Keyboard_Backspace", "symbol": "<Backspace>", "ascii": 0x08, },
    0x2B: {"desc": "Keyboard_Tab", "symbol": "<Tab>", "ascii": 0x09, },
    0x2C: {"desc": "Keyboard_KongGe", "symbol": "<SPACE>", "ascii": 0x20, },

    0x2D: {"desc": "Keyboard_JianHao", "symbol": "-", "ascii": 0x2D, "upper_symbol": "_", "upper_ascii": 0x5F, },
    0x2E: {"desc": "Keyboard_DengHao", "symbol": "=", "ascii": 0x3D, "upper_symbol": "+", "upper_ascii": 0x2B, },
    0x2F: {"desc": "Keyboard_ZuoZhongKuoHao", "symbol": "[", "ascii": 0x5B, "upper_symbol": "{", "upper_ascii": 0x7B, },
    0x30: {"desc": "Keyboard_YouZhongKuoHao", "symbol": "]", "ascii": 0x5D, "upper_symbol": "}", "upper_ascii": 0x7D, },
    0x31: {"desc": "Keyboard_FanXieGang", "symbol": "\\", "ascii": 0x5C, "upper_symbol": "|", "upper_ascii": 0x7C, },
    0x33: {"desc": "Keyboard_FenHao", "symbol": ";", "ascii": 0x3B, "upper_symbol": ":", "upper_ascii": 0x3A, },
    0x34: {"desc": "Keyboard_DanYinHao", "symbol": "\'", "ascii": 0x27, "upper_symbol": "\"", "upper_ascii": 0x22, },
    0x35: {"desc": "Keyboard_BoLangXian", "symbol": "`", "ascii": 0x60, "upper_symbol": "~", "upper_ascii": 0x7E, },
    0x36: {"desc": "Keyboard_Douhao", "symbol": ",", "ascii": 0x2C, "upper_symbol": "<", "upper_ascii": 0x3C, },
    0x37: {"desc": "Keyboard_JuHao", "symbol": ".", "ascii": 0x2E, "upper_symbol": ">", "upper_ascii": 0x3E, },
    0x38: {"desc": "Keyboard_XieGang_WenHao", "symbol": "/", "ascii": 0x2F, "upper_symbol": "?", "upper_ascii": 0x3F, },

    # function key F1-F12
    0x39: {"desc": "Keyboard_CapsLock", "symbol": "<CapsLock>", },
    0x3A: {"desc": "Keyboard_F1", "symbol": "<F1>", },
    0x3B: {"desc": "Keyboard_F2", "symbol": "<F2>", },
    0x3C: {"desc": "Keyboard_F3", "symbol": "<F3>", },
    0x3D: {"desc": "Keyboard_F4", "symbol": "<F4>", },
    0x3E: {"desc": "Keyboard_F5", "symbol": "<F5>", },
    0x3F: {"desc": "Keyboard_F6", "symbol": "<F6>", },
    0x40: {"desc": "Keyboard_F7", "symbol": "<F7>", },
    0x41: {"desc": "Keyboard_F8", "symbol": "<F8>", },
    0x42: {"desc": "Keyboard_F9", "symbol": "<F9>", },
    0x43: {"desc": "Keyboard_F10", "symbol": "<F10>", },
    0x44: {"desc": "Keyboard_F11", "symbol": "<F11>", },
    0x45: {"desc": "Keyboard_F12", "symbol": "<F12>", },

    # function key page control
    0x46: {"desc": "Keyboard_PrintScreen", "symbol": "<PrintScreen>", },
    0x47: {"desc": "Keyboard_ScrollLock", "symbol": "<ScrollLock>", },
    0x48: {"desc": "Keyboard_Pause", "symbol": "<Pause>", },
    0x49: {"desc": "Keyboard_Insert", "symbol": "<Insert>", },
    0x4A: {"desc": "Keyboard_Home", "symbol": "<Home>", },
    0x4B: {"desc": "Keyboard_PageUp", "symbol": "<PageUp>", },
    0x4C: {"desc": "Keyboard_Delete", "symbol": "<Delete>", "ascii": 0x7F, },
    0x4D: {"desc": "Keyboard_End", "symbol": "<End>", },
    0x4E: {"desc": "Keyboard_PageDown", "symbol": "<PageDown>", },
    0x4F: {"desc": "Keyboard_RightArrow", "symbol": "<RightArrow>", },
    0x50: {"desc": "Keyboard_LeftArrow", "symbol": "<LeftArrow>", },
    0x51: {"desc": "Keyboard_DownArrow", "symbol": "<DownArrow>", },
    0x52: {"desc": "Keyboard_UpArrow", "symbol": "<UpArrow>", },

    # keypad 0-9 +-*/.
    0x53: {"desc": "Keypad_NumLock", "symbol": "<NumLock>", },
    0x54: {"desc": "Keypad_ChuHao", "symbol": "/", "ascii": 0x2F, },
    0x55: {"desc": "Keypad_ChengHao", "symbol": "*", "ascii": 0x2A, },
    0x56: {"desc": "Keypad_JianHao", "symbol": "-", "ascii": 0x2D, },
    0x57: {"desc": "Keypad_JiaHao", "symbol": "+", "ascii": 0x2B, },
    0x58: {"desc": "Keypad_Enter", "symbol": "<Enter>", "ascii": 0x0D, },
    0x59: {"desc": "Keypad_1_and_End", "symbol": "1", "ascii": 0x31, },
    0x5A: {"desc": "Keypad_2_and_DownArrow", "symbol": "2", "ascii": 0x32, },
    0x5B: {"desc": "Keypad_3_and_PageDn", "symbol": "3", "ascii": 0x33, },
    0x5C: {"desc": "Keypad_4_and_LeftArrow", "symbol": "4", "ascii": 0x34, },
    0x5D: {"desc": "Keypad_5", "symbol": "5", "ascii": 0x35, },
    0x5E: {"desc": "Keypad_6_and_RightArrow", "symbol": "6", "ascii": 0x36, },
    0x5F: {"desc": "Keypad_7_and_Home", "symbol": "7", "ascii": 0x37, },
    0x60: {"desc": "Keypad_8_and_UpArrow", "symbol": "8", "ascii": 0x38, },
    0x61: {"desc": "Keypad_9_and_PageUp", "symbol": "9", "ascii": 0x39, },
    0x62: {"desc": "Keypad_0_and_Insert", "symbol": "0", "ascii": 0x30, },
    0x63: {"desc": "Keypad_Dian_and_Delete", "symbol": ".", "ascii": 0x2E, },

    # Ctrl Alt Shift Windows App
    0x65: {"desc": "Keyboard_Application", "symbol": "<Application>", },
    0xE0: {"desc": "Keyboard_LeftControl", "symbol": "<LeftControl>", },
    0xE1: {"desc": "Keyboard_LeftShift", "symbol": "<LeftShift>", },
    0xE2: {"desc": "Keyboard_LeftAlt", "symbol": "<LeftAlt>", },
    0xE3: {"desc": "Keyboard_LeftWindows", "symbol": "<LeftWindows>", },
    0xE4: {"desc": "Keyboard_RightControl", "symbol": "<RightControl>", },
    0xE5: {"desc": "Keyboard_RightShift", "symbol": "<RightShift>", },
    0xE6: {"desc": "Keyboard_RightAlt", "symbol": "<RightAlt>", },
    0xE7: {"desc": "Keyboard_RightWindows", "symbol": "<RightWindows>", },
}

KEYBOARD_TYPE = []


def process_cmd_argv(argv):
    argv_dict = {}
    pcapfile = None
    mode = None
    try:
        opts, args = getopt.getopt(argv, "hf:m:", ["pcapfile=","mode="])
    except getopt.GetoptError:
        print(USAGE)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(USAGE)
            sys.exit()
        elif opt in ("-f", "--pcapfile"):
            argv_dict['pcapfile'] = arg
        elif opt in ("-m", "--mode"):
            argv_dict['mode'] = arg

    if argv_dict.get('pcapfile') and argv_dict.get('mode'):
        return argv_dict
    else:
        print(USAGE)
        sys.exit(2)

def extract_hiddata(pcap_filename):
    '''
    tshark -r pcapfile.pcap -T fields -e usb.capdata > pcapfile.pcap.txt
    extract usb mouse hid data 4 bytes (hex) every data frame
    '''
    outfile = str(pcap_filename) + ".txt"
    # cmd = "tshark -r %s -T fields -e usb.capdata > %s" % (pcap_filename, outfile)
    cmd = "tshark -r %s -T fields -e usbhid.data > %s" % (
        pcap_filename, outfile)
    echo = os.popen(cmd).read()
    print(echo)

def process_mouse_data(line):
    btn_code = int(line[0:2], 16)
    x = int(line[2:4], 16)
    y = int(line[4:6], 16)

    if x > 127:
        x -= 256
    if y > 127:
        y -= 256
    y = -y  # screen display

    x_all, y_all, colors_all = \
        MOUSE_LOCUS.get('all').get('x'), \
        MOUSE_LOCUS.get('all').get('y'),\
        MOUSE_LOCUS.get('all').get('colors')
    x, y = x_all[-1] + x, y_all[-1] + y
    x_all.append(x)
    y_all.append(y)

    if 0x00 == (0x03 & btn_code):
        mouse_move = MOUSE_LOCUS.get('move')
        mouse_move.get('x').append(x)
        mouse_move.get('y').append(y)
        colors_all.append(MOUSE_LOCUS.get('move').get('color'))
    elif 0x01 == (0x03 & btn_code):
        mouse_left = MOUSE_LOCUS.get('left')
        mouse_left.get('x').append(x)
        mouse_left.get('y').append(y)
        colors_all.append(MOUSE_LOCUS.get('left').get('color'))
    elif 0x02 == (0x03 & btn_code):
        mouse_right = MOUSE_LOCUS.get('right')
        mouse_right.get('x').append(x)
        mouse_right.get('y').append(y)
        colors_all.append(MOUSE_LOCUS.get('right').get('color'))
    elif 0x03 == (0x03 & btn_code):
        mouse_both = MOUSE_LOCUS.get('both')
        mouse_both.get('x').append(x)
        mouse_both.get('y').append(y)
        colors_all.append(MOUSE_LOCUS.get('both').get('color'))
    else:
        print(btn_code)

def process_keyboard_data(line):
    '''
    process one keyboard data package
    byte1 indecate <Ctrl><Shift><Alt><GUI>
    byte3 indecate the key
    '''
    byte1, byte3 = int(line[0:2], 16), int(line[4:6], 16)
    if KEYBOARD_MAP.get(byte3):
        func_code, key_symbol = byte1, KEYBOARD_MAP.get(byte3).get("symbol")
    else:
        func_code, key_symbol = byte1, None
    pass

    func_symbol = ""
    if (0x01 == 0x01 & func_code) or (0x10 == 0x10 & func_code):
        func_symbol += "<Ctrl>"
    if (0x02 == 0x02 & func_code) or (0x20 == 0x20 & func_code):
        func_symbol += "<Shift>"
    if (0x04 == 0x04 & func_code) or (0x40 == 0x40 & func_code):
        func_symbol += "<Alt>"
    if (0x08 == 0x08 & func_code) or (0x80 == 0x80 & func_code):
        func_symbol += "<GUI>"

    # <Shift>+a or <Shift>
    if key_symbol:
        keyboard_type = func_symbol + key_symbol
    else:
        keyboard_type = func_symbol

    # only record the data not null
    if keyboard_type:
        KEYBOARD_TYPE.append(keyboard_type + "\n")

def process_file_data(filename):
    '''
    read usb.capdata(hex) to memory and fill all & move & left & right
    every capdata contians 4 bytes data
    1st byte represent button down: 0x00==move 0x01==Left 0x02==Right
    2nd byte represent horizontal step -128~127 px
    3rd byte represent vertial setp -128~127 px
    '''
    with open(filename, encoding='utf-8') as f:
        lines = f.readlines()    
        for line in lines:
            if 9 == len(line):
                process_mouse_data(line)
            elif 17 == len(line):
                process_keyboard_data(line)
               
def draw_mouse_locus(x, y, c, filename):
    x, y, c = np.array(x), np.array(y), np.array(c)
    plt.figure()
    plt.scatter(x, y, s=1, c=c)
    plt.axis('equal')
    plt.grid(linestyle='--')
    plt.savefig('./%s' % filename)

def write_keyboard_type(filename):
    with open(filename, 'w') as f:
        f.writelines(KEYBOARD_TYPE)



def main(argv):
    argv_dict = process_cmd_argv(argv)
    extract_hiddata(argv_dict['pcapfile'])
    process_file_data(str(argv_dict['pcapfile'])+".txt")

    mode = argv_dict['mode']

    if 'all' == mode:
        c = MOUSE_LOCUS.get(mode).get('colors')
    else:
        c = [MOUSE_LOCUS.get(mode).get('color')] * len(MOUSE_LOCUS.get(mode).get('x'))
    mouse_fig = str(argv_dict['pcapfile']) + "_mouse.png"
    draw_mouse_locus(
        x=MOUSE_LOCUS.get(mode).get('x'),
        y=MOUSE_LOCUS.get(mode).get('y'), 
        c=c,
        filename=mouse_fig
        )

    keyboard_txt = str(argv_dict['pcapfile']) + "_keyboard.txt"
    write_keyboard_type(keyboard_txt)

if __name__ == '__main__':
    main(sys.argv[1:])
