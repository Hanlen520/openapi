#coding=utf-8
#author='Shichao-Dong'

import requests,time
import hashlib
'''
https://openapi.waiqin365.com/api/{应用编码}/{应用版本}/{接口编码}/{openid}/{timestamp}/{disgest}/{msg_id}
openid   8956884185640496350
appkey   A85yRFPsUTCtwW5ESU
timestamp     请求消息时间，格式为：yyyyMMddHHmmSS如：20140701142836
digest   数据签名，使用32位小写字母，用于验证数据的真实性。数据校验码生成规则：md5(消息体|appkey|timestamp),
msg_id = "ADDorg123456"

'''
timestamp = time.strftime('%Y%m%d%H%M%S')
print timestamp


msg_id = "ADDorg123456"
data ="{'store_code': 'CUS002997'}"
openid  = '8956884185640496350'
appkey  = 'A85yRFPsUTCtwW5ESU'


print data
m= hashlib.md5()
dg = str(data) + "|" + appkey + "|" + timestamp
print dg
m.update(dg)
psw = m.hexdigest()
print psw

base_url = "http://172.31.3.231:6020/api/store/v1/queryStore/"
url = base_url + openid + '/' + timestamp + '/' + psw + '/' + msg_id
print url
# url = "http://172.31.3.231:6020/api/store/v1/queryStore/8956884185640496350/20171115174006/1223508142d9e0250ef654ea3d88fc6b/ADDorg123456"

headers = { "content-type": "application/json",
            }

r = requests.post(url=url,headers = headers,data=data)
print r.text


# import requests
#
# url = "http://172.31.3.231:6020/api/store/v1/queryStore/8956884185640496350/20171115174006/1223508142d9e0250ef654ea3d88fc6b/ADDorg123456"
# payload ="{'store_code': 'CUS002997'}"
#
# m= hashlib.md5()
# dg = str(payload) + "|" + appkey + "|" + '20171115174006'
# print dg
# m.update(dg)
# psw = m.hexdigest()
#
# base_url = "http://172.31.3.231:6020/api/store/v1/queryStore/"
# url = base_url + openid + '/' + '20171115174006' + '/' + psw + '/' + msg_id
# print url
#
# # payload = "{\"store_code\": \"CUS002997\"}\r\n\r\n"
# headers = {
#     'content-type': "application/json",
#     # 'cache-control': "no-cache",
#     # 'postman-token': "d7635aa5-68ff-3f1d-0a2e-1ecd0faa2744"
#     }
#
# response = requests.request("POST", url, data=payload, headers=headers)
#
# print(response.text)