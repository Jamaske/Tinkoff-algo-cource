#include <cstdint>
#include <deque>
#include <iostream>
#include <string>  // Include the string library for std::stoi
#include <unordered_map>

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    uint64_t N;
    std::cin >> N;
    std::cin.ignore(1);
    std::unordered_map<uint32_t, uint32_t> id_pos(N >> 5);
    std::deque<uint32_t> que(N >> 5);
    uint32_t ticket_prvider = 0, ticket_gatherer = 0;
    uint32_t param;
    char buff[9] = {};
    for (uint64_t i = 0; i < N; ++i) {
        std::cin.getline(buff, sizeof(buff));
        switch (buff[0]) {
        case '1':  // new human
            param = std::stoi(buff + 2);
            que.push_front(param);
            id_pos[param] = ticket_prvider++;
            break;

        case '2':  // human done
            id_pos.extract(que.back());
            que.pop_back();
            ticket_gatherer += 1;
            break;

        case '3':  // human inpation
            id_pos.extract(que.front());
            que.pop_front();
            ticket_prvider -= 1;
            break;

        case '4':  // human waiting
            param = std::stoi(buff + 2);
            std::cout << id_pos[param] - ticket_gatherer << '\n';
            break;

        case '5':  // next human
            std::cout << que.front() << '\n';
            break;
        }
    }
}
