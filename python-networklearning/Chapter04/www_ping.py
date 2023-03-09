import argparse, socket, sys


def connect_to(hostname_or_ip):
    try:
        infolist = socket.getaddrinfo(hostname_or_ip, 'www', 0, socket.SOCK_STREAM, 0, socket.AI_ADDRCONFIG | socket.AI_V4MAPPED | socket.AI_CANONNAME)
    except socket.gaierror as e:  # 名称服务错误
        print('Name service failure: ', e.args[1])
        sys.exit(1)

    print(infolist)
    info = infolist[0]
    socket_args = info[0:3]
    address = info[4]
    s = socket.socket(*socket_args)

    try:
        s.connect(address)
    except socket.error as e:  # 网络故障
        print('Network failure: ', e.args[1])
    else:
        print('Success: host ', info[3], 'is listening on port 80')


if __name__ == '__main__':
    parse = argparse.ArgumentParser(description='Try connectibg to port 80')
    parse.add_argument('hostname', help='hostname that you want to contact')
    connect_to(parse.parse_args().hostname)
