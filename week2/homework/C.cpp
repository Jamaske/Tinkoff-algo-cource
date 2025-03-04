#include <cstdint>
#include <iostream>
// #include <unistd.h>
#include <stack>

constexpr uint64_t BufferSize = 4096;
int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::string buffer;
    std::cin >> buffer;
    uint32_t i = 0;
    uint32_t end = buffer.length();
    char ch = buffer[i];
    std::stack < int,
        while (i < end) {
        switch (ch)  // decide on parser type
        {
        case '+':
        case '*':


            break;

        default:
            break;
        }
    }
}
return 0;
}
