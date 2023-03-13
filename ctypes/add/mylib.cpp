#include <iostream>

// 定义一个函数
extern "C" int add(int a, int b) {
    std::cout << "add(" << a << ", " << b << ")" << std::endl;
    return a + b;
}

