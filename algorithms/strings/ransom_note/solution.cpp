// Hash Tables: Ransom Note
//
// author: Dela Anthonio
// hackerrank: https://hackerrank.com/delaanthonio
// problem: https://www.hackerrank.com/challenges/ctci-ransom-note/problem

#include <algorithm>
#include <cmath>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <unordered_map>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    int m;
    int n;
    string word;
    unordered_map<string, int> magazine;
    unordered_map<string, int> note;

    cin >> m >> n;

    for (int i = 0; i < m; i++) {
        cin >> word;
        magazine[word]++;
    }

    for (int i = 0; i < n; i++) {
        cin >> word;
        if (++note[word] > magazine[word]) {
            cout << "No";
            return 0;
        }
    }

    cout << "Yes";
    return 0;
}
