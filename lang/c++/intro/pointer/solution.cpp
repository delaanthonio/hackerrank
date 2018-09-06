// Pointer
//
// author: Dela Anthonio
// hackerrank: https://hackerrank.com/delaanthonio
// problem: https://hackerrank.com/challenges/c-tutorial-pointer

#include <cmath>
#include <iostream>

using namespace std;

void update(int *a, int *b) {
    int sum = *a + *b;
    int abs_diff = abs(*a - *b);
    *a = sum;
    *b = abs_diff;
}

int main() {
    ios_base::sync_with_stdio(false);
    int a;
    int b;
    cin >> a >> b;
    update(&a, &b);
    cout << a << endl << b << endl;
    return 0;
}
