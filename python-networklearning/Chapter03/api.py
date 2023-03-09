import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 调用 makefile 生成文件描述符
sockfd = sock.makefile()
print(hasattr(sock, 'read'), hasattr(sockfd, 'read'))