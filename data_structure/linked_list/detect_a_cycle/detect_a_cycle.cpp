/**
 * @problem https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem
 */

struct Node {
    int data;
    struct Node* next;
};

bool has_cycle(Node* head) {
    Node* fast = head;
    Node* slow = head;

    while (fast && fast->next) {
        fast = fast->next->next;
        slow = slow->next;
        if (fast == slow) {
            return true;
        }
    }
    return false;
}
