import select, zen_util


def all_events_forever(poll_object):
    while True:
        for fd, event in poll_object.poll():
            yield fd, event


def server(listener):
    sockets = {listener.fileno(): listener}
    addresses = {}
    bytes_received = {}
    bytes_to_send = {}

    poll_object = select.poll()
    poll_object.register(listener, select.POLLIN)

    for fd, event in all_events_forever(poll_object):
        sock = sockets[fd]

        if event & (select.POLLHUP | select.POLLERR | select.POLLNVAL):
            address = addresses.pop(sock)
            rb = bytes_received.pop(sock, b'')
            sb = bytes_to_send.pop(sock, b'')
            if rb:
                print(f"Client {address} sent {rb} but then closed")
            elif sb:
                print(f"Client {address} closed before we sent {sb}")
            else:
                print(f"Client {address} closed socket normally")
            poll_object.unregister(fd)
            del sockets[fd]
        elif sock is listener:
            conn, conn_address = sock.accept()
            print(f"Accepted connections from {conn_address}")
            conn.setblocking(False)
            sockets[conn.fileno()] = conn
            addresses[conn] = conn_address
            poll_object.register(conn, select.POLLIN)
        elif event & select.POLLIN:
            more_data = sock.recv(4096)
            if not more_data:
                sock.close()
                continue
            data = bytes_received.pop(sock, b'') + more_data
            if data.endswith(b'?'):
                bytes_to_send[sock] = zen_util.get_answer(data)
                poll_object.modify(sock, select.POLLOUT)
            else:
                bytes_received[sock] = data
        elif event & select.POLLOUT:
            data = bytes_to_send.pop(sock)
            n = sock.send(data)
            if n < len(data):
                bytes_to_send[sock] = data[n:]
            else:
                poll_object.modify(sock, select.POLLIN)


if __name__ == '__main__':
    address = zen_util.parse_command_line('low-level async server')
    listener = zen_util.create_srv_socket(address)
    server(listener)
