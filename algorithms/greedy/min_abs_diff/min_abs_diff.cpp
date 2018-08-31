
#include <algorithm>
#include <cmath>
#include <iostream>
#include <iterator>
#include <limits>
#include <numeric>
#include <vector>
using namespace std;

int main() {
    int n;
    vector<int> arr;
    int min_abs_diff = INT32_MAX;
    cin >> n;
    copy_n(istream_iterator<int>(cin), n, back_inserter(arr));
    sort(begin(arr), end(arr));
    for (auto i = 0; i < arr.size() - 1; i++) {
        min_abs_diff = min(min_abs_diff, abs(arr[i] - arr[i + 1]));
    }
    cout << min_abs_diff;
    return 0;
}
