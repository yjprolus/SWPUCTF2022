base64_list = ['0', '1', '2', '3', '4', '5', '=', 'A', 'D', 'E', 'G', 'I', 'M', 'N', 'O', 'Q', 'R', 'T', 'U',
               'V', 'W', 'Y', 'Z', 'c', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'x', 'y', 'z']


def encode_ascii(string: str) -> str:
    temp = ''
    base = ''

    # 把原始字符串转换为二进制，用bin转换后去掉开头的0b，首位补0补齐8位
    for i in string:
        temp += '{:08}'.format(int(str(bin(ord(i))).replace('0b', '')))

    # 6位一组截取，最后一组不足6位的后面补0，获取base_list中对应的字符
    for j in range(0, len(temp), 6):
        t = '{:<06}'.format(temp[j: j + 6])
        base += base64_list[int(t, 2)]

    # 判断base字符长度结尾补‘=’
    if len(string) % 3 == 1:
        base += '=='
    elif len(string) % 3 == 2:
        base += '='
    return base


def decode_ascii(base: str) -> str:
    temp = ''
    string = ''

    # 去掉尾补的‘=’
    base = base.replace('=', '')
    # 获取base在base_list中的索引，转换为二进制，用bin转换后去掉开头的0b，首位补0补齐6位
    for s in range(len(base)):
        temp += '{:06}'.format(
            int(str(bin(base64_list.index(base[s]))).replace('0b', '')))

    # 8位一组截取（已忽略最后一组），转10进制，获取ASCII字符
    for i in range(len(temp) // 8):
        string += chr(int(temp[8 * i: 8 * i + 8], 2))

    return string


# 使用utf8支持中文
def encode(string: str, encoding: str = 'utf8') -> str:
    temp = ''
    base = ''

    # 获取字符串编码
    string = string.encode(encoding)

    # 把字符串编码为二进制，用bin转换后去掉开头的0b，首位补0补齐8位
    for i in string:
        temp += '{:08}'.format(int(str(bin(i)).replace('0b', '')))

    # 6位一组截取，最后一组不足6位的后面补0，获取base_list中对应的字符
    for j in range(0, len(temp), 6):
        t = '{:<06}'.format(temp[j: j + 6])
        base += base64_list[int(t, 2)]

    # 判断base字符长度结尾补‘=’
    if len(string) % 3 == 1:
        base += '=='
    elif len(string) % 3 == 2:
        base += '='
    return base


def decode(base: str, encoding: str = 'utf8') -> str:
    temp = ''
    string_bytes = []

    # 去掉尾补的‘=’
    base = base.replace('=', '')
    # 获取base在base_list中的索引，转换为二进制，用bin转换后去掉开头的0b，首位补0补齐6位
    for s in range(len(base)):
        temp += '{:06}'.format(
            int(str(bin(base64_list.index(base[s]))).replace('0b', '')))

    # 8位一组截取（已忽略最后一组），转10进制
    for i in range(len(temp) // 8):
        string_bytes.append(int(temp[8 * i: 8 * i + 8], 2))

    # 根据编码获取源字符串
    return bytes(string_bytes).decode(encoding)


# Demo
v = '人人a'
print(v)

v = encode(v)
print(v)

v = decode(v)
print(v)
