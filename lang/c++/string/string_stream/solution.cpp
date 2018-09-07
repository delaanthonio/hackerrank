// StringStream
//
// author: Dela Anthonio
// hackerrank: https://hackerrank.com/delaanthonio
// problem: https://hackerrank.com/challenges/c-tutorial-stringstream

#include <iostream>
#include <sstream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);

    string str;
    int num;
    cin >> str;
    stringstream ss(str);

    while (ss >> num) {
        cout << num << endl;
        ss.ignore(); // ignore commas
    }

    return 0;
}
