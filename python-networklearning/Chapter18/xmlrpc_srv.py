import operator, math
from xmlrpc.server import SimpleXMLRPCServer
from functools import reduce


def addtogether(*things):
    return reduce(operator.add, things)


def quadratic(a, b, c):
    b24ac = math.sqrt((b * b) - 4.0 * a * c)
    return list(set([(-b-b24ac) / 2.0 * a, (-b+b24ac) / 2.0 * a]))


def remote_repr(arg):
    return arg


def main():
    server = SimpleXMLRPCServer(('127.0.0.1', 7001))

    server.register_introspection_functions()  # 自省
    server.register_multicall_functions()  # 允许将多个独立的函数调用打包在同一个网络往返中
    server.register_function(addtogether)
    server.register_function(quadratic)
    server.register_function(remote_repr)
    print('Server ready')
    server.serve_forever()


if __name__ == '__main__':
    main()