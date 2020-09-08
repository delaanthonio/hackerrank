// New Keyboard locked
//
// author: Dela Anthonio
// hackerrank: https://hackerrank.com/delaanthonio
// problem:
// https://www.hackerrank.com/contests/hack-the-interview-v/challenges/strange-keyboard-1/problem

#include <algorithm>
#include <bits/stdc++.h>
#include <cmath>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <vector>

using namespace std;

void receivedText(string& raw) {
    stack<string> output;
    bool numLock = true;
    string back = "";
    string* out = &back;

    for (char const& c : raw) {
        if (c == '<') {
            output.push("");
            out = &output.top();
        } else if (c == '>') {
            out = &back;
        } else if (c == '*') {
            out->pop_back();
        } else if (c == '#') {
            numLock = !numLock;
        } else if (numLock || !isdigit(c)) {
            out->push_back(c);
        }
    }

    ofstream fout(getenv("OUTPUT_PATH"));
    while (output.size()) {
        fout << output.top();
        output.pop();
    }
    fout << back;
    fout.close();
}

int main() {
    ios_base::sync_with_stdio(false);

    string S;
    getline(cin, S);
    ofstream fout(getenv("OUTPUT_PATH"));

    receivedText(S);
    fout.close();

    return 0;
}
