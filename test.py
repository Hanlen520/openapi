#coding=utf-8
#author='Shichao-Dong'

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import yaml
import requests
import hashlib
import time
import json

def readyaml():
    #读取yaml配置文件内容
    f = open('data.yaml')
    data = yaml.load(f)
    f.close()
    # print data['common']['baseurl']
    # print data
    return data

def digest():
    timestamp = time.strftime('%Y%m%d%H%M%S')

    openid = readyaml()['common']['openid']
    appkey = readyaml()['common']['appkey']
    msg_id = readyaml()['common']['msg_id']
    base_url =readyaml()['common']['baseurl']
    data = readyaml()['payload'][0]['data']
    print str(data.decode('utf-8'))
    # 加密生成url
    m= hashlib.md5()
    dg = str(data.decode('utf-8')) + "|" + appkey + "|" + timestamp
    m.update(dg)
    psw = m.hexdigest()

    url = base_url + openid + '/' + timestamp + '/' + psw + '/' + msg_id
    print url
    return url

def postreq():
    headers = { "content-type": "application/json",
            }
    data = readyaml()['payload'][0]['data']
    url = digest()
    r = requests.post(url=url,headers = headers,data=str(data.decode('utf-8')))
    print r.content
    if json.loads(r.content)['return_code']== 0:
        print 'Pass'
    else:
        print 'Fail'

if __name__=="__main__":
    postreq()