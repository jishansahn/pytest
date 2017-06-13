import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

base_url='https://www.zuihuibao.cn/zhb_pay_test/extend/bf_query_callback_extend/'
# read from file
f=open("./order_no.txt",'r', encoding='utf-8',errors='ignore')

order_no_list = f.readlines()
s=requests.session()
for order_no in order_no_list:
    real_url = base_url+order_no
    print(real_url)
    resp = s.get(real_url,verify=False)
    print(resp.content)
    # r_json = resp.json('result')
    # print(s.cert)
    # print(r_json['code'], ':', r_json['result'])