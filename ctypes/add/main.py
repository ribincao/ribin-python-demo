import ctypes

# 加载共享库
mylib = ctypes.CDLL('./libmylib.so')


# 调用共享库中的add函数
result = mylib.add(2, 3)

# 输出结果
print(result)

