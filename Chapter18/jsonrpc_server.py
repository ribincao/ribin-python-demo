from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer


def lengths(*args):
    """MEasure the length of each input argument."""
    results = []
    for arg in args:
        try:
            arglen = len(arg)
        except TypeError:
            arglen = None
        results.append((arglen, arg))
    return results


def main():
    server = SimpleJSONRPCServer(('localhost', 7002))
    server.register_function(lengths)
    print("Starting server")
    server.serve_forever()


#  jsonrpc 只支持列表这一顺序结构
if __name__ == '__main__':
    main()