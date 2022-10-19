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


data = [ 115, 119, 112, 117, 123, 114, 99, 52, 95, 49, 115, 95, 101, 52, 115, 121, 125]
flag = input('请输入flag：')
key = 'wllm'
sBox = init(key)
flag = str_to_data(flag)
res = rc4_crypt(flag, sBox)
if flag == res:
    print('yes')
else:
    print('wrong')