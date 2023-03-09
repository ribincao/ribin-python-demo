

def demo():
    b = bytes([0, 1, 98, 99, 100])  # 字节字符串对象
    print(len(b), type(b), list(b), b)


def ascii_demo():
    for i in range(32, 128, 32):
        print(' '.join(chr(j) for j in range(i, i + 32)))


def endian_demo():
    import struct
    print("hex: ", hex(4253))
    #  箭头指向低位字节
    print("small endian: ", struct.pack('<i', 4253))
    print("big endian: ", struct.pack('>i', 4253))

    print("small endian: ", struct.unpack('<i', b'\x9d\x10\x00\x00'))
    print("big endian: ", struct.unpack('>i', b'\x00\x00\x10\x9d'))


def serial_demo():
    import json
    print(json.dumps([51, 'ribincao'], ensure_ascii=False))
    print(json.loads('{"name": "ribincao", "age": 27}'))


def zip_demo():
    import zlib
    data = zlib.compress(b'Python') + b'.' + zlib.compress(b'zlib') + b'.'
    print(data)


# 单字节编码 | 多字节编码
if __name__ == '__main__':
    zip_demo()
