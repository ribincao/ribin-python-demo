import memcache

def memcache_demo():
    mc = memcache.Client(['127.0.0.1:11211'])  # 假设 11211 端口运行着内存缓存守护进程
    mc.set('user:19', 'Simple is better than complex')  # 写入其他 python 对象会自动触发 memcache 的 pickle 操作
    print(mc.get('user:19'))


if __name__ == '__main__':
    memcache_demo()
    
    #  pip3 install python3-memcached