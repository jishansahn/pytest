import requests

# POST https://www.zuihuibao.cn/yiiapp/message/inform HTTP/1.1
# Host: www.zuihuibao.cn
# Proxy-Connection: keep-alive
# Content-Length: 0
# Connection: keep-alive
# Accept-Language: zh-Hans, en-us
# Cookie: user_id=910; ZHBSESSID=94df4734c45ed87482021237efe7ad74; Hm_lvt_31949ddc1f8c28d09bc5ee5c26938369=1493175044,1493175149,1493186858,1493263260
# User-Agent: zuihuibao/1.0.0 CFNetwork/711.3.18 Darwin/14.0.0
s=requests.session()

cookies=dict(ZHBSESSID='94df4734c45ed87482021237efe7ad74')

# rsp=requests.post('https://www.zuihuibao.cn/yiiapp/message/inform',cookies=cookies,verify=False)

s.cookies=requests.cookies.cookiejar_from_dict(cookies, cookiejar=None, overwrite=True)
rsp2=s.post('https://www.zuihuibao.cn/yiiapp/message/inform',cert=('./certifile/ssl-bundle.crt','./certifile/ssl.key'))
rsp3=s.post('https://www.zuihuibao.cn/yiiapp/message/inform',cert=('./certifile/ssl-bundle.crt','./certifile/ssl.key'))

print(rsp2.text)
print(rsp3.text)
# POST https://www.zuihuibao.cn/yiiapp/message/inform HTTP/1.1
# Host: www.zuihuibao.cn
# Accept: */*
# Connection: keep-alive
# Accept-Encoding: gzip, deflate
# User-Agent: python-requests/2.11.1
# Cookie: ZHBSESSID=94df4734c45ed87482021237efe7ad74
# Content-Length: 0