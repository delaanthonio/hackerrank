// Highest Value Palindrome
//
// author: Dela Anthonio
// hackerrank: https://hackerrank.com/delaanthonio
// problem: https://www.hackerrank.com/challenges/richie-rich/

#include <bits/stdc++.h>
#include <string>

using namespace std;

string highest_palindrome(int n, int k, string s) {
    set<int> fixed;

    for (int l = 0, r = n - 1; l < r; ++l, --r) {
        if (s[l] != s[r]) {
            if (k == 0) {
                return "-1";
            }
            s[l] = max(s[l], s[r]);
            s[r] = max(s[l], s[r]);
            fixed.insert(l);
            --k;
        }
    }

    for (int l = 0, r = n - 1; l <= r and k; ++l, --r) {
        if (s[l] == '9') {
            continue;
        } else if (fixed.count(l) or l == r) {
            s[l] = '9';
            s[r] = '9';
            k--;
        } else if (k >= 2) {
            s[l] = '9';
            s[r] = '9';
            k -= 2;
        }
    }

    return s;
}

int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(false);
    int n;
    int k;
    string s;

    cin >> n >> k >> s;
    string output = highest_palindrome(n, k, s);
    cout << output;
    return 0;
}
