import base64
from Crypto.Cipher import AES
# from flag import getflag
iv = '1229002635654321'
key = 'nssctfneedcrypto'
# data = getflag()
data = "nssctf{aaaadfaf}"


def pad(data):
    pad_data = data
    for i in range(0, 16 - len(data)):
        pad_data = pad_data + ' '
    return pad_data


def AES_en(key, data):
    if len(data) < 16:
        data = pad(data)
    AES_obj = AES.new(key.encode("utf-8"), AES.MODE_CBC, iv.encode("utf-8"))
    AES_en_str = AES_obj.encrypt(data.encode("utf-8"))
    AES_en_str = base64.b64encode(AES_en_str)
    AES_en_str = AES_en_str.decode("utf-8")
    return AES_en_str


data = AES_en(key, data)
print(data)
print(pad(data))
print(AES_en(key, pad(data)))
# data=862EoKZMO3sqpNlzyvIW5G/8MFeAI/zgGXcgi5eNOL8=
