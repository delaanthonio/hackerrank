/*
 * https://www.hackerrank.com/contests/c-programming-test-1/challenges/finding-factorial-of-n-number
 */

#include <stdio.h>

int main()
{
    int n;
    int ftl = 1;

    scanf("%d", &n);

    for (int i = 1; i <= n; i++) {
        ftl *= i;
    }

    printf("%d", ftl);

    return 0;
}
