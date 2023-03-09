import zen_util
from threading import Thread


def start_threads(listener, workers=4):
    t = (listener, )
    for i in range(workers):
        Thread(target=zen_util.accept_connections_forever, args=t).start()


if __name__ == '__main__':
    address = zen_util.parse_command_line('simple multi-threaded server')
    listener = zen_util.create_srv_socket(address)
    start_threads(listener)

    # python3 -m trace -tg --ignore-dir=/usr srv_single.py ''