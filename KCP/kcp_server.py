import socket
from kcp import KCP



def main():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_sock.bind(('127.0.0.1', 12345))
    server_kcp = KCP(123, server_sock)
    server_kcp.update()
    server_kcp.send(b'world')
    server_kcp.update()
    server_sock.close()


main()
