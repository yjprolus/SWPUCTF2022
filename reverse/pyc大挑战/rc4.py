# uncompyle6 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)]
# Embedded file name: rc4.py
# Compiled at: 2022-10-01 13:23:45
# Size of source mod 2**32: 1065 bytes


def init(key):
    sBox = []
    index = 0
    k = []
    for i in range(256):
        sBox.append(i)
        k.append(ord(key[(i % len(key))]))

    for i in range(256):
        index = (index + sBox[i] + k[i]) % 256
        sBox[i], sBox[index] = sBox[index], sBox[i]

    return sBox


def rc4_crypt(data, sBox):
    i = 0
    j = 0
    t = 0
    for k in range(len(data)):
        i = (i + 1) % 256
        j = (j + sBox[i]) % 256
        sBox[i], sBox[j] = sBox[j], sBox[i]
        t = (sBox[i] + sBox[j]) % 256
        data[k] ^= sBox[t]

    return data


def data_to_str(data):
    str = ''
    for i in range(len(data)):
        str += chr(data[i])

    return str


def str_to_data(str):
    d = []
    for i in range(len(str)):
        d.append(ord(str[i]))

    return d


data = [
 115, 119, 112, 117, 123, 114, 99, 52, 95, 49, 115, 95, 101, 52, 115, 121, 125]
# flag = input('请输入flag：')
flag="nssctf{dfadfdasf}"
key = 'wllm'
sBox = init(key)
print(sBox)
flag = str_to_data(flag)
print(flag)
res = rc4_crypt(flag, sBox)
# print(res)
# if flag == res:
#     print('yes')
# else:
#     print('wrong')