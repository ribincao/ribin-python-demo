import argparse, socket, sys


def server(host, port, bytecount):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(1)
    print(f"Listen at {sock.getsockname()}")
    while True:
        conn, sockname = sock.accept()
        print('Processing up to 1024 bytes at a time from  ', sockname)
        n = 0
        while True:
            data = conn.recv(1024)  # 数据少于 1024 也会返回
            if not data:
                break
            output = data.decode('ascii').upper().encode('ascii')
            conn.sendall(output)
            n += len(data)
            print('\r %d bytes processed so far' %(n, ), end=' ')
            sys.stdout.flush()
        print()
        conn.close()
        print(' Socket closed')


def client(host, port, bytecount):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bytecount = (bytecount + 15) // 16 * 16 # round up to a multiple of 16
    message = b'capitalize this!'

    print('Sending', bytecount, 'bytes of data, in chunks of 16 bytes')
    sock.connect((host, port))
    sent = 0
    # 发送较大数据时候死锁在发送阶段而没有去接收数据
    while sent < bytecount:
        sock.sendall(message)
        sent += len(message)
        print('\r %d bytes sent' % (sent, ), end=' ')
        sys.stdout.flush()
    print()
    sock.shutdown(socket.SHUT_WR)

    print('Receiving all the data the server sends back')

    received = 0
    while True:
        data = sock.recv(42)
        if not received:
            print(' The first data received says', repr(data))
        if not data:
            break
        received += len(data)
        print('\r %d bytes received' %(received, ), end=' ')
    print()
    sock.close()


if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive over TCP')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='interface the server listen; host the client sends to')
    parser.add_argument('bytecount', type=int, nargs='?', default=16, help='number of bytes for client to send (default 16)')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060, help='TCP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p, args.bytecount)