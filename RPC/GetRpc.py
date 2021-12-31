import frida, sys



js = open('rpc.js', 'r', encoding='utf8').read()
def on_message(message, data):
    print(message)
    if message['type'] == 'send':
        pass
    else:
        pass

device = frida.get_remote_device()  # .attach("com.smile.gifmaker")
yitian = "com.kwai.m2u"
session = device.attach(yitian)
script = session.create_script(js)
script.on("message", on_message)
script.load()
result = script.exports.encode("POST&app=m2u&appver=2.5.2.20520&boardPlatform=sdm845&brand=OnePlus&ch=ALIBABA&channel=ALIBABA&device=ONEPLUS+A6000&deviceId=5128fa1aa8d91937d03165655c1610f4&did=ANDROID_1c21b0cb4941fc77&egid=DFP607314346C37E67F4C43C51BF6EB6D6525CCA6D4FBF72DFD765BBE0CAE259&fr=ANDROID&globalid=DFP607314346C37E67F4C43C51BF6EB6D6525CCA6D4FBF72DFD765BBE0CAE259&isdg=0&md=ONEPLUS A6000&od=91A01047BF6962FA8F05288481ED46F4A8A0AEB9C8DDD5CE6744E06BDCD600A4&os=ANDROID_10&platform=android&sr=1080*2075&type=fairyTale&umid=&ve=2.5.2.20520&ver_code=20520&wifi=<unknown ssid>&-3555709364547267446")
print(result)