#coding: utf-8
import hashlib
dic = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-'
dic0=dic.to
for a in dic:
    for b in dic:
        for c in dic:
            for d in dic:
                # flag = 'Boom_MD5' + str(a) + str(b) + + str(c) + + str(d)
                flag = 'Boom_MD5'+a+b+c+d
                md5 = hashlib.md5(flag.encode('utf-8')).hexdigest()
                if md5[:27] == "0618ac93d4631df725bceea74d0":
                    print(flag)
print("over")
# data = 'Boom_MD5****'
# Boom_MD5_NSS
# 0618ac93d4631df725bceea74d0*****
# 0618ac93d4631df725bceea74d0fe071
