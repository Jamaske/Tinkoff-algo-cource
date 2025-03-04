#include <cstdint>
#include <iostream>

struct min_queue {
    const uint32_t len;
    uint32_t sep;
    int32_t InMin;
    // cyclic data queue
    int* const data;

    // steals data array
    min_queue(uint32_t len)
        : len(len),
          sep(len),
          InMin(INT32_MAX),
          // In data | Out min
          data(reinterpret_cast<int*>(malloc((len + 1) * sizeof(int)))) {
        // edge case guardian value
        data[len] = INT32_MAX;
    }

    // push and pop from the queue
    void step(int new_val) {
        if (sep == len) {
            InMin = INT32_MAX;
            while (--sep)
                data[sep] = (InMin = std::min(InMin, data[sep]));
            InMin = new_val;
        } else
            InMin = std::min(InMin, new_val);
        data[sep] = new_val;
        ++sep;
    }

    // return minimum of the queue
    int min() {
        return std::min(InMin, data[sep]);
    }
};

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    uint32_t N, K;
    std::cin >> N >> K;
    min_queue queue(K);
    int val;
    uint32_t i = 0;
    while (i < K) {
        std::cin >> val;
        queue.step(val);
        ++i;
    }
    std::cout << queue.min() << ' ';

    while (i < N) {
        std::cin >> val;
        queue.step(val);
        std::cout << queue.min() << ' ';
        ++i;
    }
}
