import zen_util


if __name__ == '__main__':
    address = zen_util.parse_command_line('simple single-threaded server')
    listener = zen_util.create_srv_socket(address)
    zen_util.accept_connections_forever(listener)

    # python3 -m trace -tg --ignore-dir=/usr srv_single.py ''