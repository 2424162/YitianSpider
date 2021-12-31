import base64
import requests

url = "https://www.baidu.com"

headers = {
'Content-Type': 'multipart/form-data; boundary=c47d54f1-6385-45a5-a397-86ec4881d4f8',

}
pic = open("1.PNG","rb")
proxies = {'http': 'http://localhost:8888', 'https': 'http://localhost:8888'}

data = "--c47d54f1-6385-45a5-a397-86ec4881d4f8\r\n"+'Content-Disposition: form-data; name="beforeProcess";filename="beforeProcess.jpeg"\n'+"Content-Type: image/png\r\n"+"Content-Length: {}\r\n".format(str(123123))+"\r\n"+str(pic.read())+"\r\n"

requests.request("POST",headers=headers,url=url,data=data,proxies = proxies,verify=False)
print(requests.head(url))