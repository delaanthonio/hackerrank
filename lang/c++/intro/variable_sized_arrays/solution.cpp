// Variable Sized Arrays
//
// author: Dela Anthonio
// hackerrank: https://hackerrank.com/delaanthonio
// problem: https://hackerrank.com/challenges/variable-sized-arrays

#include <algorithm>
#include <iostream>
#include <iterator>
#include <numeric>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    vector<vector<int>> vectors;
    int n, q;

    cin >> n >> q;

    while (n--) {
        vector<int> vec;
        int size;
        cin >> size;
        copy_n(istream_iterator<int>(cin), size, back_inserter(vec));
        vectors.push_back(vec);
    }

    while (q--) {
        int v;
        int i;
        cin >> v >> i;
        cout << vectors[v][i] << endl;
    }

    return 0;
}
