import requests
import json
import xlrd
import pytest

# def user_login():
    # s=requests.Session()

verifyurl='https://www.zuihuibao.cn/php2/mobile/send_smscode_fix.php'
r1=requests.get(verifyurl,{'mobileNum':'10000000066'},verify=False)
ck=r1.cookies
# set cookie
# jar = requests.cookies.RequestsCookieJar()
# jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
# jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
# url = 'http://httpbin.org/cookies'
# r = requests.get(url, cookies=jar)
# r.text
# '{"cookies": {"tasty_cookie": "yum"}}'

print(r1.text)
# url='https://www.zuihuibao.cn/yiiapp/system/user-login'
# data={'mobile':'10000000066','verify_code':'9527','login_type':'2'}
# r=requests.post(url,data=data,verify=False)
#
# print(r.status_code)
    # return ck

