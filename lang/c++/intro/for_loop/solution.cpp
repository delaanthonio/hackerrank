// For Loop
//
// author: Dela Anthonio
// hackerrank: https://hackerrank.com/delaanthonio
// problem: https://hackerrank.com/challenges/c-tutorial-for-loop

#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int main() {
    int a;
    int b;
    cin >> a;
    cin >> b;
    for (int i = a; i <= b; i++) {
        string output;
        switch (i) {
        case 1:
            output = "one";
            break;
        case 2:
            output = "two";
            break;
        case 3:
            output = "three";
            break;
        case 4:
            output = "four";
            break;
        case 5:
            output = "five";
            break;
        case 6:
            output = "six";
            break;
        case 7:
            output = "seven";
            break;
        case 8:
            output = "eight";
            break;
        case 9:
            output = "nine";
            break;
        default:
            if (i % 2 == 1) {
                output = "odd";
            } else {
                output = "even";
            }
        }
        cout << output << "\n";
    }
    return 0;
}
