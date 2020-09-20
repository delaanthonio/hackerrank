// Making Candies
//
// author: Dela Anthonio
// hackerrank: https://hackerrank.com/delaanthonio
// problem: https://www.hackerrank.com/challenges/making-candies

#include <bits/stdc++.h>
#include <climits>

using ll = long long;
using namespace std;

ll int_div_ceil(ll dividend, ll divisor) {
    return (dividend + divisor - 1) / divisor;
}

ll min_passes(ll machines, ll workers, ll cost, ll goal, ll candies, ll passes = 1,
              ll best = LLONG_MAX) {
    if (candies >= goal or candies / machines < workers) {
        return min(best, passes);
    }

    ll new_candies = machines * workers;
    ll skip = max((cost - candies) / new_candies, 1LL);
    ll saving = passes + int_div_ceil(goal - candies, new_candies);
    ll capacity = machines + workers + candies / cost;
    ll half = int_div_ceil(capacity, 2);

    machines = max({machines, workers, half});
    workers = capacity - machines;

    ll next_candies = candies % cost + skip * workers * machines;
    return min_passes(machines, workers, cost, goal, next_candies, passes + skip,
                      min(best, saving));
}

int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(false);
    ll machines;
    ll workers;
    ll cost;
    ll candies;

    cin >> machines >> workers >> cost >> candies;

    ll result = min_passes(machines, workers, cost, candies, machines * workers);
    cout << result;

    return 0;
}
