#include <cstdint>
#include <iostream>
struct Node {
    int64_t val, sum;
    Node *left, *right;
    constexpr Node(int64_t val)
        : val(val),
          sum(val),
          left(nullptr),
          right(nullptr) {}
};

class Tree {
    Node* root = nullptr;

   public:
    // non duplicat insert
    void insert(int64_t val) {
        Node* cur = root;
        Node** next = &root;
        while (cur) {
            cur->sum += val;
            if (val <= cur->val)
                next = &cur->left;  // next = cur + offsetof(Node, left) in bytes
            else
                next = &cur->right;  // next = cur + offsetof(Node, right) in bytes
            cur = *next;
        }
        *next = new Node(val);
    }

    void print() {
        print(root);
    }

    void static print(Node* node, uint16_t depth = 0) {
        if (!node) return;
        if (!depth)
            std::cout << '[' << node->val << "]  " << node->sum << '\n';
        else {
            for (int i = 1; i < depth; ++i) std::cout << "|  ";
            std::cout << "|--[" << node->val << "]  " << node->sum << '\n';
        }
        print(node->left, depth + 1);
        print(node->right, depth + 1);
    }

    int64_t partial_sum(int64_t l) {
        if (!root) return 0;
        Node* cur = root;
        int64_t total = 0;
        if (cur->val <= l)
            goto start_right;
        else
            goto loop_left;

    brk2:
        if (cur->val < l) {
        start_right:
            total += cur->sum;
        loop_right:
            cur = cur->right;
            if (!cur) goto exit;
            if (!(cur->val < l)) goto brk1;
            goto loop_right;
        } else {
            total += cur->val;
            if (cur->left) total += cur->left->sum;
            goto exit;
        }
    brk1:
        if (cur->val > l) {
            total -= cur->sum;
        loop_left:
            cur = cur->left;
            if (!cur) goto exit;
            if (!(cur->val > l)) goto brk2;
            goto loop_left;
        } else if (cur->right)
            total -= cur->right->sum;
    exit:
        return total;
    }

    int64_t range_sum(int64_t l, int64_t r) {
        return partial_sum(r) - partial_sum(l - 1);
    }
}

;


int main() {
    Tree tree;
    tree.insert(4);
    tree.insert(2);
    tree.insert(1);
    tree.insert(3);
    tree.insert(6);
    tree.insert(5);
    tree.insert(7);
    tree.print();
    // std::cout << tree.range_sum(3, 6) << std::endl;
    std::cout << tree.partial_sum(4) << std::endl;
}