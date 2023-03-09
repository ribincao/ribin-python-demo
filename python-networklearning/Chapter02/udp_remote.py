import argparse, socket, random, sys

MAX_BYTES = 65535


def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((interface, port))
    print(f'Listening at {sock.getsockname()}')
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        if random.random() < 0.5:
            print(f"Pretending to drop packet from {address}")
            continue
        text = data.decode('ascii')
        print("The client at {} says {!r}".format(address, text))
        message = f'Your data was {len(data)} bytes long'
        sock.sendto(message.encode('ascii'), address)


def client(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hostname = sys.argv[2]
    sock.connect((hostname, port))
    print(f'Client socket name is {sock.getsockname()}')

    delay = 0.1
    text = 'This is another message'
    data = text.encode('ascii')
    while True:
        sock.send(data)
        print(f'Waitting up to {delay} seconds for a reply')
        sock.settimeout(delay)
        try:
            data = sock.recv(MAX_BYTES)
        except socket.timeout:
            delay *= 2
            if delay > 2.0:
                raise RuntimeError('I think the server is down')
        else:
            break
    print('THe server says {!r}'.format(data.decode('ascii')))

if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive UDP locally')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('host', help='interface the server listen;''host the client sends to')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060, help='UDP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)
    # python3 udp_remote.py server ""
    # python3 udp_remote.py client "www.ribincao.com"

    # python3 udp_remote.py server 172.16.0.14
    # python3 udp_remote.py server 127.0.0.1
    # python3 udp_remote.py client "www.ribincao.com"
    # python3 udp_remote.py client 172.16.0.14
    # python3 udp_remote.py client 127.0.0.1
