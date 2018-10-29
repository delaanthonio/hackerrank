// Construct the Array
//
// author: Dela Anthonio
// hackerrank: https://hackerrank.com/delaanthonio
// problem: https://www.hackerrank.com/challenges/construct-the-array

#include <algorithm>
#include <cmath>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <vector>

using namespace std;

const long LIMIT = 1e9 + 7;

long count_ways(int n, int k, int x) {
    vector<long> ways_end_k{1};
    vector<long> ways_end_1{0};
    for (int i = 0; i < n - 2; i++) {
        ways_end_k.push_back((ways_end_k[i] * (k - 2) + ways_end_1[i]) % LIMIT);
        ways_end_1.push_back((ways_end_k[i] * (k - 1)) % LIMIT);
    }
    if (x == 1) {
        return ways_end_1.back();
    }
    return ways_end_k.back();
}

int main() {
    ios_base::sync_with_stdio(false);
    int n;
    int k;
    int x;
    cin >> n >> k >> x;
    cout << count_ways(n, k, x);
    return 0;
}
