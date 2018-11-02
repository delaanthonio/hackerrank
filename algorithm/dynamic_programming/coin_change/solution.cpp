// The Coin Change Problem
//
// author: Dela Anthonio
// hackerrank: https://hackerrank.com/delaanthonio
// problem: https://www.hackerrank.com/challenges/coin-change/problem

#include <algorithm>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <vector>
using namespace std;

long long coin_change(int amount, int size, int coins[]) {
    long long *ways = (long long *)calloc(amount + 1, sizeof(*ways));
    ways[0] = 1;
    for (int i = 0; i < size; i++) {
        int coin = coins[i];
        for (int j = coin; j <= amount; j++) {
            ways[j] += ways[j - coin];
        }
    }
    free(ways);
    return ways[amount];
}

int main() {
    int m, n;
    cin >> m >> n;
    int coins[n];
    for (int i = 0; i < n; i++) {
        cin >> coins[i];
    }
    long long ways = coin_change(m, n, coins);
    cout << ways << endl;
    return 0;
}
