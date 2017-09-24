/*
 * https://www.hackerrank.com/contests/c-programming-test-1/challenges/finding-the-fibanocci-of-n-number
 */

#include <stdio.h>

int main()
{
    int a, b, c;

    scanf("%d,%d,%d", &a, &b, &c);

    int max = a;

    if (b > max)
        max = b;

    if (c > max)
        max = c;

    printf("%d", max);

    return 0;
}
