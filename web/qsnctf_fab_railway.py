import math
import re
import socket

HOST, PORT = "challenge.qsnctf.com", 34998


def cal_fab(n):
    '''
    计算斐波那契数列通项
    '''
    result = (((1 + math.sqrt(5)) / 2) ** n - ((1 - math.sqrt(5)) / 2) ** n) / math.sqrt(5)
    return int(result)


def sum_fab(n):
    """
    斐波那契数列求和公式sum(n)=2*f(n)+f(n-1)-1
    """
    result = 2 * cal_fab(n) + cal_fab(n - 1) - 1
    return result


def cal_u(n, m, a):
    """
    计算未知参数u
    """
    if 4 == n:
        return 0  # 实际上此情况u可以是任何正整数
    elif 5 == n:
        return m - 2 * a
    elif 6 <= n:
        result = (m - 2 * a - a * sum_fab(n - 5)) / sum_fab(n - 4)
        result = int(result)
        return result
    else:
        return None


def cal_stay(n, a, u, x):
    """
    计算第x站上车人数
    """
    if 1 == x or 2 == x:
        return a
    elif 3 == x:
        return 2 * a
    elif 4 == x:
        return 2 * a + u
    elif 5 <= x < n:
        return 2 * a + a * sum_fab(x - 4) + u * sum_fab(x - 3)
    elif n == x:
        return 0
    else:
        return None


def solve(n, m, a, x):
    u = cal_u(n, m, a)
    return cal_stay(n, a, u, x)


def get_n_a_m_x(text):
    match = re.search(
        r'Stations \(n\): (\d+)\s*Initial \(a\): (\d+)\s*Total at n-1 \(m\): (\d+)\s*Target station \(x\): (\d+)', text,
        re.DOTALL)
    if match:
        n, a, m, x = map(int, match.groups())
        return n, a, m, x
    return None, None, None, None


def unit_test():
    # 单元测试计算斐波那契数列
    for n in range(1, 10):
        print(f'fab({n}): {cal_fab(n)} sum({n})={sum_fab(n)}')

    # 单元测试获取数据
    text_welcome = b'Welcome to the Train Logistic Challenge!'.decode("utf-8")
    n, a, m, x = get_n_a_m_x(text_welcome)
    print(f'n={n}, a={a}, m={m}, x={x}')  # n=None, a=None, m=None, x=None
    text1 = b"\nSolve 100 rounds of the 'Train Problem' to get the flag.\nRules: You have 1.5s per round. Good luck!\n\n--- Round [1/100] ---\nStations (n): 15\nInitial (a): 9\nTotal at n-1 (m): 6873\nTarget station (x): 4\nYour answer for station 4: ".decode(
        "utf-8")
    n, a, m, x = get_n_a_m_x(text1)
    print(f'n={n}, a={a}, m={m}, x={x}')  # n=15, a=9, m=6873, x=4

    # 单元测试计算u
    u = cal_u(n, m, a)
    print(f'u={u}')  # u=24

    # 单元测试计算stay
    sx = cal_stay(n, a, u, x)
    print(f'S({x})={sx}')  # S(4)=42


def conn_recv_send(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((host, port))
        while True:
            data = sock.recv(1024)
            data_str = None
            if data:
                data_str = data.decode("utf-8")
                print(data_str)
            if data_str and (-1 != data_str.find('qsnctf{') or -1 != data_str.find('Wrong!')):
                break
            elif data_str and -1 != data_str.find('Your answer for station'):
                n, a, m, x = get_n_a_m_x(data_str)
                result = solve(n, m, a, x)
                print(result)
                sock.send(str(result).encode("utf-8") + b'\n')
            else:
                continue
    except socket.timeout:
        print(f"Time Out!")
    except ConnectionRefusedError:
        print(f"Connection Refused!")
    except Exception as e:
        print(f'Error:\n{e}')
    finally:
        sock.close()
    pass


if __name__ == '__main__':
    conn_recv_send(HOST, PORT)
    # unit_test()
