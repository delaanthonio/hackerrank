// The Coin Change Problem
//
// author: Dela Anthonio
// hackerrank: https://hackerrank.com/delaanthonio
// problem: https://www.hackerrank.com/challenges/coin-change

#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

long long coin_change(int amount, vector<int> coins) {
    vector<long long> ways(amount + 1);
    ways[0] = 1;

    for (auto coin = begin(coins); coin != end(coins); coin++) {
        for (int j = *coin; j <= amount; j++) {
            ways[j] += ways[j - *coin];
        }
    }

    return ways.back();
}

int main() {
    int m, n;
    cin >> m >> n;
    vector<int> coins(n);

    for (int i = 0; i < n; i++) {
        cin >> coins[i];
    }

    long long ways = coin_change(m, coins);
    cout << ways << endl;
    return 0;
}
