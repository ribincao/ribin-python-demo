from socketserver import BaseRequestHandler, TCPServer, ThreadingMixIn
import zen_util


class ZenHandler(BaseRequestHandler):
    def handle(self):
        zen_util.handle_conversation(self.request, self.client_address)


# 使用 ForkingMixIn 代替 ThreadingMixIn 改为多进程
class ZenServer(ThreadingMixIn, TCPServer):
    allow_reuse_address = 1
    # address_family = socket.AF_INET6


if __name__ == '__main__':
    address = zen_util.parse_command_line('legacy "SocketServer" server')
    server = ZenServer(address, ZenHandler)
    server.serve_forever()
