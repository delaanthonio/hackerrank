/*
 * https://www.hackerrank.com/contests/c-programming-test-1/challenges/finding-sum-of-n-numbers
 */

#include <stdio.h>

int main()
{
    int n;

    scanf("%d", &n);

    int sum = 0;

    for (int i = n; i > 0; i--) {
        sum += i;
    }

    printf("%d", sum);

    return 0;
}
