// Queues: A Tale of Two Stacks
//
// author: Dela Anthonio
// hackerrank: https://hackerrank.com/delaanthonio
// problem: https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks

#include <iostream>
#include <algorithm>
#include <stack>
using namespace std;

class DualStackQueue {

private:
    stack<int> recent;
    stack <int> oldest;

    void populate_oldest() {
        if (oldest.empty()) {
            while(not recent.empty()) {
                oldest.push(recent.top());
                recent.pop();
            }
        }
    }

public:
    void push(int x) {
        recent.push(x);
    }

    void pop() {
        populate_oldest();
        oldest.pop();
    }

    int front() {
        populate_oldest();
        return oldest.top();
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    DualStackQueue dsq;
    int q, type, x;
    cin >> q;

    for(int i = 0; i < q; i++) {
        cin >> type;
        if(type == 1) {
            cin >> x;
            dsq.push(x);
        }
        else if(type == 2) {
            dsq.pop();
        }
        else cout << dsq.front() << endl;
    }
    return 0;
}
