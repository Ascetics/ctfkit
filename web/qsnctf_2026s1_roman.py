import socket

HOST, PORT = 'challenge.qsnctf.com', 34148


def roman_to_num(text):
    '''
    罗马数字转整数
    欢迎来到编程世界！
    你将连接到一个交互式服务。在每一轮中，服务端会向你提供一个罗马数字，你的任务是将其正确转换为对应的整数。请使用NC连接。
    '''
    tab = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    list_num1 = []
    for c in text:  # 第一遍循环，从罗马数字字母到数字
        list_num1.append(tab.get(c))

    list_num2, left_num, temp_sum = [], 0, 00
    for n in list_num1:  # 第二遍循环，把相邻相同的数字加和
        if left_num == 0:  # 第一个数的情况
            left_num = n
            temp_sum = n
        elif left_num == n:  # 和左边数字相同，加和
            temp_sum += n
        elif left_num != n:  # 和左边数字不同，把和放进去
            list_num2.append(temp_sum)
            left_num = n
            temp_sum = n
    if temp_sum != 0:  # 最后一个加和放进去
        list_num2.append(temp_sum)

    num, left_num = 0, 0
    for n in list_num2:  # 第三遍循环，左小-，左大+
        if left_num == 0:
            left_num = n
        elif left_num < n:
            num -= left_num
            left_num = n
        elif left_num > n:
            num += left_num
            left_num = n
    num += left_num  # 最后一个数
    print(num)
    return num


def get_roman_text(data_str):
    texts = data_str.split('\n')
    return texts[2]


def conn_recv_send(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
        while True:
            data = sock.recv(1024)
            if data:
                data_str = data.decode()
                print(data_str)
                if -1 != data_str.find('Round'):
                    roman_text = get_roman_text(data_str)
                    print(roman_text)
                    num = roman_to_num(roman_text)
                    sock.send(str(num).encode() + b'\n')
                if -1 != data_str.find('Congratulations'):
                    break
    except socket.timeout:
        print(f'Time Out!')
    except ConnectionRefusedError:
        print(f'Connection Refused!')
    except Exception as e:
        print(f'Error!\n{e}')
    pass


if __name__ == '__main__':
    conn_recv_send(HOST, PORT)
    # roman_to_num('MMMLXV')  # 3065
    # roman_to_num('MMDCCLIV')  # 2754
    # roman_to_num('MMCXL')  # 2140
    # roman_to_num('MMMCCCI')  # 3301
    # roman_to_num('MMDCCLI')  # 2751
    # roman_to_num('MCDLXXVIII')  # 1478
