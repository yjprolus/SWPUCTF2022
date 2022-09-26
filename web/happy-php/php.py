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
python ch_md5.py "666666" 0   
61146528383226743337

?jiangnaij=61146528383226743337&csc8=57

'''