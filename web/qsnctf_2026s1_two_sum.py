import socket

HOST, PORT = 'challenge.qsnctf.com', 33799


def solve_two_sum(list_nums, target_num):
    for idx1 in range(len(list_nums)):
        for idx2 in range(idx1 + 1, len(list_nums)):
            num1, num2 = list_nums[idx1], list_nums[idx2]
            if target_num == num1 + num2:
                answer = f'({idx1},{idx2},{num1},{num2})'
                return answer


def solve_two_sum_pro(list_nums, target_num):
    '''
    这个效率更高
    '''
    dict_nums = dict()
    for idx, num in enumerate(list_nums):
        dict_nums[num] = idx
    for num1, idx1 in dict_nums.items():
        num2 = target_num - num1
        idx2 = dict_nums.get(num2)
        if idx2 and idx2 != idx1:
            answer = f'({idx1},{idx2},{num1},{num2})'
            return answer
    return None


def process_data_str(data_str):
    lines = data_str.split('\n')
    list_nums = []
    target_num = None
    for line in lines:
        line = line.strip()
        if line.startswith('List = ['):
            num_strs = line[8:-1].split(',')
            for num_str in num_strs:
                list_nums.append(int(num_str))
            print(list_nums)
        if line.startswith('Target ='):
            target_num = int(line[9:])
            print(target_num)
    return list_nums, target_num


def connect_and_receive(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    try:
        sock.connect((host, port))
        print('Connection Established! 连接建立！')
        while True:
            data = sock.recv(1024)
            data_str = None
            if data:
                data_str = data.decode('utf-8')
                print(data_str)
                if -1 != data_str.find('Congratulations! Here is your flag:'):  # 答题完成收到Congratulations就跳出循环
                    break
            if data_str and -1 != data_str.find('List') and -1 != data_str.find('Target'):
                list_nums, target_num = process_data_str(data_str)
                answer = solve_two_sum_pro(list_nums, target_num)
                if answer:
                    print(f'答案：{answer}')
                    answer += '\n'
                    sock.sendall(answer.encode('utf-8'))
    except socket.timeout:
        print('Connection Time Out! 连接超时！')
    except ConnectionResetError:
        print('ConnectionResetError! 连接被拒绝！')
    except Exception as e:
        print(f'Error:{e}')
    finally:
        sock.close()


if __name__ == '__main__':
    connect_and_receive(HOST, PORT)
