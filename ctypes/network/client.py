import socket

HOST = 'localhost'
PORT = 12345

# 创建socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接到服务器
client_socket.connect((HOST, PORT))

# 发送消息
message = 'Hello from Python'
client_socket.send(message.encode())

# 接收回复消息并打印
response = client_socket.recv(1024)
print(response.decode())

# 关闭socket
client_socket.close()

