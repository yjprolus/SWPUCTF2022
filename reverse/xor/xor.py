key='SWPU'
flag=''
result=[32,32,32,32,40,46,63,32,12,48,53,33,12,36,96,39,33,46,119,38,12,49,60,52,52,42]
for i in range(len(result)):
    flag+=chr(result[i]^ord(key[i%4]))
print(flag)