// Swap Nodes [Algo]
//
// author: Dela Anthonio
// hackerrank: https://hackerrank.com/delaanthonio
// problem: https://www.hackerrank.com/challenges/swap-nodes-algo

#include <bits/stdc++.h>
#include <utility>
#define pii pair<int, int>
using namespace std;

void swap_nodes(vector<pii>& tree, int k, int n = 0, int height = 1) {
    int l = tree[n].first;
    int r = tree[n].second;
    if (l >= 0) {
        swap_nodes(tree, k, l, height + 1);
    }
    if (r >= 0) {
        swap_nodes(tree, k, r, height + 1);
    }
    if (height % k == 0) {
        tree[n] = make_pair(r, l);
    }
}

void traverse_tree(vector<pair<int, int>>& tree, int n = 0) {
    int l = tree[n].first;
    int r = tree[n].second;
    if (l >= 0) {
        traverse_tree(tree, l);
    }
    cout << n + 1 << " ";
    if (r >= 0) {
        traverse_tree(tree, r);
    }
}

int main() {
    cin.tie(0);
    ios_base::sync_with_stdio(false);
    int n;
    int q;
    int first;
    int second;
    cin >> n;
    vector<pair<int, int>> tree(n);
    for (int i = 0; i < n; ++i) {
        cin >> first >> second;
        tree[i] = make_pair(first - 1, second - 1);
    }
    cin >> q;
    for (int i = 0; i < q; ++i) {
        cin >> first;
        swap_nodes(tree, first);
        traverse_tree(tree);
        cout << endl;
    }
    return 0;
}
