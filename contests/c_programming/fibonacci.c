/*
 * https://www.hackerrank.com/contests/c-programming-test-1/challenges/finding-the-fibanocci-of-n-number
 */

#include <stdio.h>

int main()
{
    int n;

    scanf("%d", &n);

    int fib[10000] = {0};

    fib[0] = 0;
    fib[1] = 1;

    printf("01");

    /* if (n == 1) { */
    /*     return 0; */
    /* } */

    for (int i = 2; i <= n; ++i) {
        fib[i] = fib[i - 1] + fib[i - 2];
        printf("%d", fib[i]);
    }


    return 0;
}
