#include <iostream>

int main() {
    char a[10];
    std::cin >> a;
    int val = 0;
    int i = 0;
    while (i < 10) {
        char ch = a[i];
        if (ch == '\n') break;
        val = val * 10 + (ch - 0x30);
        i = i + 1;
    }

    std::cout << val << '\n';
}