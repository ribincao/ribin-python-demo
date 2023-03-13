// server.cpp
#include <iostream>
#include <cstring>
#include <unistd.h>
#include <sys/socket.h>
#include <arpa/inet.h>

int main()
{
    // 创建socket
    int server_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (server_fd < 0) {
        std::cerr << "Failed to create socket" << std::endl;
        return 1;
    }

    // 设置socket选项
    int opt = 1;
    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &opt, sizeof(opt))) {
        std::cerr << "Failed to set socket options" << std::endl;
        return 1;
    }

    // 绑定socket到本地地址
    struct sockaddr_in address;
    memset(&address, 0, sizeof(address));
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(12345);
    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address)) < 0) {
        std::cerr << "Failed to bind socket to address" << std::endl;
        return 1;
    }

    // 监听socket
    if (listen(server_fd, 5) < 0) {
        std::cerr << "Failed to listen on socket" << std::endl;
        return 1;
    }

    // 接受连接并处理请求
    std::cout << "Server is running on port 12345" << std::endl;
    while (true) {
        int client_fd = accept(server_fd, NULL, NULL);
        if (client_fd < 0) {
            std::cerr << "Failed to accept incoming connection" << std::endl;
            continue;
        }
        char buffer[1024] = {0};
        int bytes_received = read(client_fd, buffer, sizeof(buffer));
        if (bytes_received < 0) {
            std::cerr << "Failed to read from socket" << std::endl;
            close(client_fd);
            continue;
        }
        std::cout << "Received message: " << buffer << std::endl;
        const char *response = "Hello from C++";
        int bytes_sent = write(client_fd, response, strlen(response));
        if (bytes_sent < 0) {
            std::cerr << "Failed to write to socket" << std::endl;
        }
        close(client_fd);
    }

    // 关闭socket
    close(server_fd);
    return 0;
}

