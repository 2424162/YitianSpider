import time
import random
import base64
import frida
from urllib import parse
from HeadersConfig import config
import requests
import os
def init():
    js = open('rpc.js', 'r', encoding='utf8').read()
    device = frida.get_remote_device()
    yitian = "com.kwai.m2u"
    session = device.attach(yitian)
    script = session.create_script(js)
    script.load()
    return script

def get_nonce():
    t = time.time()
    i = int(int(round(t*1000))/60000)
    random.seed(t)
    i2 = random.randint(100000000,2222222222)
    value = i | (i2 << 32)
    return value

def get_sig2_string():
    sig2_str = ""
    url_header = {}
    header = config().get_header()
    for key in sorted(header):
        sig2_str = sig2_str+key+"="+header[key]+"&"
    sig2_str = sig2_str+str(get_nonce())
    return sig2_str

def get_sig2_header(script):
    sig2 = get_sig2_string()
    sign = script.exports.encode(sig2)
    bytes1 = bytearray(sign,encoding="utf-8")
    bytes2 = nonce_tobyte(get_nonce())
    print(bytes1)
    print(type(bytes1))
    print(bytes1+bytes2)
    base64_sig2 = base64.encodebytes(bytes2+bytes1)
    sig = base64_sig2.decode("utf-8")

    final_sig2 = sig.replace("+","-").replace("/","_").replace("=","")
    return final_sig2

def nonce_tobyte(num):
    longtime = num
    arr = [0,0,0,0,0,0,0,0]
    for i in range(7,-1,-1):
        arr[i] = int_to_byte(255 & int(longtime))
        longtime >>= 8
    for i in range(0, len(arr)):
        if arr[i]<0:
            arr[i] = -arr[i]
    b = bytearray(arr)
    return b


def int_to_byte(num):
    result = ''
    int_s = bin(num).replace("0b",'')
    if(len(int_s)<8):
        size = 8-len(int_s)
        int_s = '0'*size+int_s
    if(int_s[0]==str(0)):
        mbyte=(int(int_s,2))
    else:
        for i in int_s[1:]:
            if i == str(1):
                result = result + "0"
            else:
                result = result + "1"
        mbyte = -(int(result,2)+1)
    return mbyte


def headers_to_url(sig2):
    header = config().get_header()
    header.update({"__clientSign2": sig2})
    url_tail = parse.urlencode(header)
    return url_tail


def request_yitian(tail):
    url = "https://m2u-api.getkwai.com/api-server/api/v1/genericProcess?"+tail
    #url = "https://www.baidu.com"+tail
    headers = {
        'app-id': '27',
        'Connection': 'keep-alive',
        'Accept-Language': 'zh-cn',
        'Content-Type': 'multipart/form-data; boundary=c47d54f1-6385-45a5-a397-86ec4881d4f8',
        'Accept-Encoding': 'gzip'
    }
    pic = open("pic/14.png", "rb")
    size = os.path.getsize("pic/144.png")
    data = "--c47d54f1-6385-45a5-a397-86ec4881d4f8\r\n"+'Content-Disposition: form-data; name="beforeProcess";filename="beforeProcess.jpeg"\n'+"Content-Type: image/jpeg\r\n"+"Content-Length: {}\r\n".format(str(size))+"\r\n"+str(pic.read())+"\r\n"

    response = requests.request("POST",url=url,headers=headers,data=data,verify=False)
    print(response.url)
    print(response)
    print(response.content)


if __name__ == '__main__':
    script = init()
    sig2 = get_sig2_header(script)
    url_tail = headers_to_url(sig2)

    request_yitian(url_tail)

