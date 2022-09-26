import base64
a = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ+/'
b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
c = '2T3M3xJr3wqT4tfeuenTq9mNwBvOsdzJ1hQ='
table = str.maketrans(a,b)
d = c.translate(table)
data = base64.b64decode(d)
print(data)