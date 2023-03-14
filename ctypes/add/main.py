import ctypes

# 加载共享库
mylib = ctypes.CDLL('./libmylib.so')

# 定义函数签名和类型注释
mylib.add.argtypes = (ctypes.c_int, ctypes.c_int)
mylib.add.restype = ctypes.c_int


# 定义Python函数，调用C++ DLL中的函数
def add(x: int, y: int) -> int:
    return mylib.add(x, y)


# 调用共享库中的add函数
result = mylib.add(2, 3)

# 输出结果
print(result)

