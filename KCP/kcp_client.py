import socket
from kcp import KCP


def main():
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_kcp = KCP(123, client_sock)
    client_kcp.send(b'hello')
    client_kcp.update()
    client_kcp.update()
    client_sock.close()


main()
