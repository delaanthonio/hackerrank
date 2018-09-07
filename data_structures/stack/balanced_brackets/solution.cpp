// Balanced Brackets
//
// author: Dela Anthonio
// hackerrank: https://hackerrank.com/delaanthonio
// problem: https://www.hackerrank.com/challenges/balanced-brackets

#include <algorithm>
#include <cmath>
#include <iostream>
#include <iterator>
#include <sstream>
#include <stack>
#include <vector>

using namespace std;

// Return whether `brackets` is balanced.
//
// time: O(n)
// space: O(n)
bool is_balanced(string brackets) {
    stringstream ss(brackets);
    char bracket;
    stack<char> unmatched;
    while (ss >> bracket) {
        char expected;
        switch (bracket) {
        case '{':
        case '[':
        case '(':
            unmatched.push(bracket);
            continue;
        case '}':
            expected = '{';
            break;
        case ']':
            expected = '[';
            break;
        case ')':
            expected = '(';
            break;
        }
        if (unmatched.empty() or unmatched.top() != expected) {
            return false;
        }
        unmatched.pop();
    }
    return unmatched.empty();
}

int main() {
    ios_base::sync_with_stdio(false);
    int n;
    cin >> n;
    string brackets;
    for (int i = 0; i < n; i++) {
        cin >> brackets;
        if (is_balanced(brackets)) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }
    return 0;
}
