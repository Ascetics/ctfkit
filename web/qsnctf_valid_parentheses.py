import socket
import re

HOST, PORT = "challenge.qsnctf.com", 34283


def process_parentheses(parentheses):
    '''
    欢迎来到编程世界！
    你将连接到一个交互式服务。
    在每一轮中，服务端会向你提供一个只包含括号字符的字符串。
    你的任务是判断该字符串是否为一个有效的括号序列。
    '''
    round_count = 0  # 圆括号()
    square_count = 0  # 方括号[]
    curly_count = 0  # 花括号{}
    for p in parentheses:
        if p == '(':
            round_count += 1
        elif p == ')':
            if 0 >= round_count:
                return False
            else:
                round_count -= 1
        elif p == '[':
            square_count += 1
        elif p == ']':
            if 0 >= square_count:
                return False
            else:
                square_count -= 1
        elif p == '{':
            curly_count += 1
        elif p == '}':
            if 0 >= curly_count:
                return False
            else:
                curly_count -= 1
    return 0 == round_count and 0 == square_count and 0 == curly_count


def get_parentheses(data_str):
    if data_str:
        return data_str.split('\n')[-2]


def conn_recv_send(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    data, data_str = None, None
    try:
        sock.connect((host, port))
        while True:
            data = sock.recv(1024)
            if data:
                data_str = data.decode()
            if data_str and (-1 != data_str.find('qsnctf{')
                             or -1 != data_str.find('Wrong!')):
                print(data_str)
                break
            if -1 != data_str.find('You need to determine whether the bracket string I give is valid.') \
                    or -1 != data_str.find('Congratulations!'):
                print(data_str)
                continue

            # 本例不是每次发送一个完整的数据，所以要拼接，以'Input> '为结束的依据
            buffer = ''
            while -1 == data_str.find('Input> '):
                buffer += data_str
                data_str = sock.recv(1024).decode()
            buffer += data_str
            print(buffer)

            parentheses = get_parentheses(buffer)
            result = process_parentheses(parentheses)
            print(f'{result}')
            sock.send(str(result).encode() + b'\n')
    except socket.timeout:
        print(f'Connection timed out!')
    except ConnectionRefusedError:
        print(f'Connection refused!')
    finally:
        sock.close()
    pass


if __name__ == '__main__':
    conn_recv_send(HOST, PORT)
    # 单元测试
    # print(process_parentheses('['))  # False
    # print(process_parentheses(''))  # True
    # print(process_parentheses('[]()'))  # True
    # print(process_parentheses('[]{}()()'))  # True
    # print(process_parentheses('[]'))  #
    # print(process_parentheses('()'))  # True
    # print(process_parentheses('(])}}{{(('))  # False
    # print(process_parentheses('(][}))][['))  # False
    # print(process_parentheses('(](]{}'))  # False
