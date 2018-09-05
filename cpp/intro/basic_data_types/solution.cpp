// Basic Data Types
//
// author: Dela Anthonio
// hackerrank: https://hackerrank.com/delaanthonio
// problem: https://hackerrank.com/challenges/c-tutorial-basic-data-types

#include <cstdio>
#include <iostream>

using namespace std;

int main() {
    int i;
    long l;
    char c;
    float f;
    double d;
    scanf("%d %ld %c %f %lf", &i, &l, &c, &f, &d);
    printf("%d\n%ld\n%c\n%.3f\n%lf\n", i, l, c, f, d);
    return 0;
}
