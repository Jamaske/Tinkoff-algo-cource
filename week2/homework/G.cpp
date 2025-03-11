#include <cstdint>
#include <iostream>


struct Node {
    Node* next;
    uint32_t id;
    constexpr Node(uint32_t id)
        : next(nullptr),
          id(id) {}
};

struct List {
    Node* start;
    Node* mid;
    Node* end;
    uint32_t size;

    constexpr List()
        : start(nullptr),
          mid(nullptr),
          end(nullptr),
          size(0) {}

    void add(uint32_t id) {
        ++size;
        if (end) {
            start = start->next = new Node(id);
            if (size & 1) mid = mid->next;
        } else {
            start = end = mid = new Node(id);
        }
    }

    uint32_t get() {  // last deletion bug
        uint32_t ret = end->id;
        end = end->next;
        if (--size & 1) mid = mid->next;

        return ret;
    }

    void insert(uint32_t id) {
        Node* new_node = new Node(id);
        ++size;
        if (end) {
            new_node->next = mid->next;
            mid->next = new_node;
            if (size & 1) mid = new_node;
        } else {
            start = end = mid = new_node;
        }
    }
};


int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    List list;
    uint64_t N;
    std::cin >> N;
    std::cin.ignore(1);
    char buff[10];

    for (uint64_t i = 0; i < N; ++i) {
        std::cin.getline(buff, 9);

        switch (buff[0]) {
        case '+':
            list.add(std::stoi(buff + 2));
            break;

        case '*':
            list.insert(std::stoi(buff + 2));
            break;

        case '-':
            std::cout << list.get() << '\n';
            break;
        }
    }
}