# Playfair密码
 
#（创建**矩阵的算法小部分参考了其他人的做法，具体加解密核心代码则为原创）
# 字母表
letter_list = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
 
# 移除字符串中重复的字母
def remove_duplicates(key):
    key = key.upper()   # 转成大写字母组成的字符串
    _key = ''
    for ch in key:
        if ch == 'J':
            ch = 'I'
        if ch in _key:
            continue
        else:
            _key += ch
    return _key
 
# 根据**建立密码表
def create_matrix(key):
    key = remove_duplicates(key)  # 移除**中的重复字母
    key = key.replace(' ', '')  # 去除**中的空格
 
    for ch in letter_list:  # 根据**获取新组合的字母表
        if ch not in key:
            key += ch
    # 密码表
    keys = [[i for j in range(5)] for i in range(5)]
    for i in range(len(key)):  # 将新的字母表里的字母逐个填入密码表中，组成5*5的矩阵
        keys[i // 5][i % 5] = key[i]  # j用来定位字母表的行
    return keys
 
# 获取字符在密码表中的位置
def get_matrix_index(ch, keys):
    for i in range(5):
        for j in range(5):
            if ch == keys[i][j]:
                return i, j   # i为行，j为列
 
def get_ctext(ch1, ch2, keys):
    index1 = get_matrix_index(ch1, keys)
    index2 = get_matrix_index(ch2, keys)
    r1, c1, r2, c2 = index1[0], index1[1], index2[0], index2[1]
    if r1 == r2:
        ch1 = keys[r1][(c1+1) % 5]
        ch2 = keys[r2][(c2+1) % 5]
    elif c1 == c2:
        ch1 = keys[(r1+1) % 5][c1]
        ch2 = keys[(r2+1) % 5][c2]
    else:
        ch1 = keys[r1][c2]
        ch2 = keys[r2][c1]
    text = ''
    text += ch1
    text += ch2
    return text
 
def get_ptext(ch1, ch2, keys):
    index1 = get_matrix_index(ch1, keys)
    index2 = get_matrix_index(ch2, keys)
    r1, c1, r2, c2 = index1[0], index1[1], index2[0], index2[1]
    if r1 == r2:
        ch1 = keys[r1][(c1-1) % 5]
        ch2 = keys[r2][(c2-1) % 5]
    elif c1 == c2:
        ch1 = keys[(r1-1) % 5][c1]
        ch2 = keys[(r2-1) % 5][c2]
    else:
        ch1 = keys[r1][c2]
        ch2 = keys[r2][c1]
    text = ''
    text += ch1
    text += ch2
    return text
 
def playfair_encode(plaintext, key):
    plaintext = plaintext.replace(" ", "")
    plaintext = plaintext.upper()
    plaintext = plaintext.replace("J", "I")
    plaintext = list(plaintext)
    plaintext.append('#')
    plaintext.append('#')
 
    keys = create_matrix(key)
    ciphertext = ''
    i = 0
    while plaintext[i] != '#':
        if plaintext[i] == plaintext[i+1]:
            plaintext.insert(i+1, 'X')
        if plaintext[i+1] == '#':
            plaintext[i+1] = 'X'
        ciphertext += get_ctext(plaintext[i], plaintext[i+1], keys)
        i += 2
    return ciphertext
 
def playfair_decode(ciphertext, key):
    keys = create_matrix(key)
    i = 0
    plaintext = ''
    while i < len(ciphertext):
        plaintext += get_ptext(ciphertext[i], ciphertext[i+1], keys)
        i += 2
    _plaintext = ''
    _plaintext += plaintext[0]
    for i in range(1, len(plaintext)-1):
        if plaintext[i] != 'X':
            _plaintext += plaintext[i]
        elif plaintext[i] == 'X':
            if plaintext[i-1] != plaintext[i+1]:
                _plaintext += plaintext[i]
    _plaintext += plaintext[-1]
    _plaintext = _plaintext.lower()
    return _plaintext
 
 
# plaintext = 'balloon'
# key = 'monarchy'
plaintext = input('明文：')
key = input('**：')
ciphertext = playfair_encode(plaintext, key)
print('加密后的密文：' + ciphertext)
plaintext = playfair_decode(ciphertext, key)
print('解密后的明文：' + plaintext)