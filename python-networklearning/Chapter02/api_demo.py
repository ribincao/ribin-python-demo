import socket


def get_port(domain):
    port = socket.getservbyname(domain)
    print(f"The port of {domain} is {port}")


if __name__ == '__main__':
    get_port('http')
