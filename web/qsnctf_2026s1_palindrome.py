import socket

HOST, PORT = 'challenge.qsnctf.com', 34094


def palindrome(text):
    '''
    回文数palindrome
    1
    121
    1221
    '''
    return text == text[::-1]


def get_num_text(data_str):
    texts = data_str.split('\n')
    return texts[2]


def conn_recv_send(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
        print(f'Connected to {host}:{port}')
        while True:
            data = sock.recv(1024)
            if data:
                data_str = data.decode()
                print(data_str)
                if -1 != data_str.find('Congratulations'):
                    break
                if -1 != data_str.find('Round'):
                    text = get_num_text(data_str)
                    result = str(palindrome(text)) + '\n'
                    sock.send(result.encode())
    except socket.timeout:
        print(f'Time Out!')
    except ConnectionRefusedError:
        print(f'Connection Refused!')
    except Exception as e:
        print(f'Error!\n{e}')
    finally:
        sock.close()


if __name__ == '__main__':
    conn_recv_send(HOST, PORT)
