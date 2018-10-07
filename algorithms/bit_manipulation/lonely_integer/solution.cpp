// Lonely Integer
//
// author: Dela Anthonio
// hackerrank: https://hackerrank.com/delaanthonio
// problem: https://www.hackerrank.com/challenges/lonely-integer

#include <algorithm>
#include <cmath>
#include <iostream>
#include <iterator>
#include <numeric>
#include <sstream>
#include <vector>

using namespace std;

int unique_num(vector<int> nums) {
    return accumulate(nums.begin(), nums.end(), 0, bit_xor<int>{});
}

int main() {
    ios_base::sync_with_stdio(false);
    int n;
    cin >> n;
    vector<int> nums;

    copy_n(istream_iterator<int>(cin), n, back_inserter(nums));
    int num = unique_num(nums);
    cout << num;

    return 0;
}
