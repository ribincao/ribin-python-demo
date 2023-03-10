import socket
import time
import struct


class KCP:
    def __init__(self, conv, sock):
        self.conv = conv
        self.sock = sock
        self.snd_una = 0
        self.snd_nxt = 0
        self.rcv_nxt = 0
        self.buffer = b''
        self.timeout = 0.1
        self.ts_flush = time.time()

    def send(self, data: bytes):
        self.buffer += data

    def flush(self):
        current = time.time()
        if current < self.ts_flush:
            return

        self.output(self.buffer)
        self.buffer = b''

        self.ts_flush = current + self.timeout

    def recv(self):
        data, addr = self.sock.recvfrom(1024)
        print(data, addr)
        conv, cmd, frg, wnd, ts, sn, una, length = struct.unpack('!IbbHIHHH', data[:20])
        data = data[20:20 + length]

        if cmd != 1:
            return None

        if conv != self.conv:
            return None

        if sn < self.rcv_nxt or sn >= self.rcv_nxt + wnd:
            return None

        self.rcv_nxt = sn + 1

        if frg == 0:
            return data

    def update(self):
        self.flush()
        while True:
            data = self.recv()
            if not data:
                break
            self.output(data)

    def output(self, data: bytes):
        while data:
            length = min(len(data), 1400)
            frg = 0 if len(data) <= 1400 else 1
            wnd = 128
            ts = int(time.time())
            pkt = struct.pack('!IbbHIHHH', self.conv, 1, frg, wnd, ts, self.snd_nxt, self.rcv_nxt, length) + data[:length]

            if self.sock.getsockname() == ('0.0.0.0', 0):
                self.sock.sendto(pkt, ("127.0.0.1", 12345)) # for client test
            else:
                self.sock.sendto(pkt, self.sock.getsockname())
            data = data[length:]

        self.snd_nxt += 1


# 示例用法
if __name__ == '__main__':
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_sock.bind(('127.0.0.1', 12345))

    server_kcp = KCP(123, server_sock)
    server_kcp.update()
    server_kcp.send(b'world')
    server_kcp.update()
    server_sock.close()

