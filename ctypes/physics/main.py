import ctypes

rp3d = ctypes.CDLL("./libreactphysics3d.so")

symbol_table = rp3d.__dict__

for symbol in symbol_table:
    print(symbol)
