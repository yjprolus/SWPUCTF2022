# python多线程爆破代码模板
import multiprocessing

def target_func(a, b):
    return a+b

pool = multiprocessing.Pool(processes=10)
pool.apply_async(target_func, (2, 3))
pool.close()
pool.join()
