import socket
import re
import json

HOST, PORT = 'challenge.qsnctf.com', 34153


def max_common_prefix(texts):
    '''
    最长公共前缀
    欢迎来到编程世界！
    你将连接到一个交互式服务。
    在每一轮中，服务端会给出一个字符串数组，你的任务是找出这些字符串的最长公共前缀。
    如果不存在公共前缀，请输出空字符串。请使用NC连接。
    '''
    min_len = min(map(len, texts))
    idx, common_prefix = 0, []
    while idx < min_len:
        t = texts[0][idx]
        for text in texts:
            if t != text[idx]:
                return ''.join(common_prefix)
        common_prefix.append(t)
        idx += 1
    return ''.join(common_prefix)


def get_list(data_str):
    match = re.search(r'\[.*\]', data_str)
    if match:
        json_str = match.group()
        str_list = json.loads(json_str)
    return str_list


def conn_recv_send(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
        while True:
            data = sock.recv(1024)
            if data:
                data_str = data.decode()
                print(data_str)
                if data_str and -1 != data_str.find('Congratulations'):
                    break
                if data_str and -1 != data_str.find('Round'):
                    texts = get_list(data_str)
                    result = max_common_prefix(texts)
                    print(result)
                    sock.send(result.encode() + b'\n')
    except socket.timeout:
        print(f'Time Out!')
    except ConnectionRefusedError:
        print(f'Connection Refused!')
    except Exception as e:
        print(f'Error!\n{e}')
    pass


if __name__ == '__main__':
    conn_recv_send(HOST, PORT)

    # 单元测试
    # data = b'\n\nRound 1:\n["rhxhqnxi", "rhxyfditbcq", "rhxybfgugtti", "rhxadckdjtt"]\n> '
    # texts = get_list(data.decode())
    # m = max_common_prefix(texts)
    # print(m)
