import argparse, socket


# 相当于 sendall
def sendval(sock, message):
    bytes_sent = 0
    while bytes_sent < len(message):
        message_remaining = message[bytes_sent:]
        bytes_sent += sock.send(message_remaining)


def recval(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError("was expecting %d bytes but only received %d bytes before the socket closed" %(length, len(data)))
        data += more
    return data


def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((interface, port))
    sock.listen(1)
    print(f"Listen at {sock.getsockname()}")
    while True:
        conn, sockname = sock.accept()
        print('We have accepted a connection from ', sockname)
        print('  Socket name: ', conn.getsockname())
        print('  Socket peer: ', conn.getpeername())
        message = recval(conn, 16)
        print('  Incoming sixteen-octet message: ', repr(message))
        conn.sendall(b'Farewell, client')
        conn.close()
        print('  Reply sent, socket closed')


def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print(f'Client has been assigned socket name ', sock.getsockname())
    sock.sendall(b'Hi there, server')
    reply = recval(sock, 16)
    print('The server said ', repr(reply))
    sock.close()


if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive over TCP')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='interface the server listen; host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060, help='TCP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)