// Conditional Statements
//
// author: Dela Anthonio
// hackerrank: https://hackerrank.com/delaanthonio
// problem: https://hackerrank.com/challenges/c-tutorial-conditional-if-else

#include <iostream>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    int n;
    cin >> n;
    if (n <= 9) {
        string num;
        switch (n) {
        case 1:
            num = "one";
            break;
        case 2:
            num = "two";
            break;
        case 3:
            num = "three";
            break;
        case 4:
            num = "four";
            break;
        case 5:
            num = "five";
            break;
        case 6:
            num = "six";
            break;
        case 7:
            num = "seven";
            break;
        case 8:
            num = "eight";
            break;
        case 9:
            num = "nine";
            break;
        }
        cout << num;
    } else {
        cout << "Greater than 9";
    }
    return 0;
}
