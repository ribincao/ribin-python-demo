import ctypes

# 加载共享库
network = ctypes.cdll.LoadLibrary('./libmylib.so')

# 调用C++函数
network.main()

