// Maximum Subarray Sum
//
// author: Dela Anthonio
// hackerrank: https://hackerrank.com/delaanthonio
// problem: https://www.hackerrank.com/challenges/maximum-subarray-sum

#include <algorithm>
#include <bits/stdc++.h>
#define ll long long
using namespace std;

ll maximum_subarray_sum(vector<ll>& arr, ll divsor) {
    ll max_sum = 0;
    ll prefix_sum = 0;
    set<ll> modulo_sum {0};

    for (auto& val : arr) {
        prefix_sum += val;
        ll modulo_val = prefix_sum % divsor;
        auto next_it = modulo_sum.upper_bound(modulo_val);
        ll next_greatest = next_it == modulo_sum.end() ? 0 : *next_it;
        max_sum = max(max_sum, (modulo_val - next_greatest + divsor) % divsor);
        modulo_sum.insert(modulo_val);
    }

    return max_sum;
}

int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(false);
    int q;
    ll divisor;
    cin >> q;
    for (int i = 0; i < q; i++) {
        int n;
        vector<ll> arr;
        cin >> n >> divisor;
        copy_n(istream_iterator<int>(cin), n, back_inserter(arr));
        ll result = maximum_subarray_sum(arr, divisor);
        cout << result << endl;
    }

    return 0;
}
