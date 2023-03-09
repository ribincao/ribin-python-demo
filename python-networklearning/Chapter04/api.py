import socket
from pprint import pprint


def get_info_list():
    infolist = socket.getaddrinfo('baidu.com', 'www')
    pprint(infolist)
    # s = socket.socket(*infolist[0][0:3])
    # s.connect(infolist[0][4])


def get_address_info():
    from socket import getaddrinfo
    print(getaddrinfo(None, 'smtp', 0, socket.SOCK_STREAM, 0, socket.AI_PASSIVE))
    print(getaddrinfo(None, 53, 0, socket.SOCK_DGRAM, 0, socket.AI_PASSIVE))

    print(getaddrinfo('127.0.0.1', 'smtp', 0, socket.SOCK_STREAM, 0))
    print(getaddrinfo('localhost', 53, 0, socket.SOCK_DGRAM, 0))


def get_host_info():
    print(socket.gethostbyname(socket.getfqdn()))  # 获取运行 python 程序机器主 IP 地址
    print(socket.gethostbyaddr('127.0.0.1'))

    print(socket.getprotobyname('UDP'))
    print(socket.getservbyname('www'))
    print(socket.getservbyport(443))


if __name__ == '__main__':
    # get_info_list()
    # get_address_info()
    get_host_info()