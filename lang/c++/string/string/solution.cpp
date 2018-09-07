// Strings
//
// author: Dela Anthonio
// hackerrank: https://hackerrank.com/delaanthonio
// problem: https://hackerrank.com/challenges/c-tutorial-strings

#include <iostream>
#include <string>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);

    string a;
    string b;
    cin >> a >> b;
    cout << a.size() << " " << b.size() << endl;
    cout << a + b << endl;
    swap(a[0], b[0]);
    cout << a << " " << b << endl;

    return 0;
}
