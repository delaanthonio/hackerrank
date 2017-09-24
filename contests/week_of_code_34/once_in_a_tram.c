/* Solution for
 * https://www.hackerrank.com/contests/w34/challenges/once-in-a-tram
 */

#include <stdio.h>

int digit_sum(int x) {
    int sum = 0;
    while (x) {
        sum += x % 10;
        x /= 10;
    }
    return sum;
}

int next_lucky_number(int x) {
    x += 1;
    int left_half = x / 1000;
    int right_half = x % 1000;
    while (digit_sum(left_half) != digit_sum(right_half)) {
        x += 1;
        left_half = x / 1000;
        right_half = x % 1000;
    }
    return x;
}

int main() {
    int x;
    scanf("%d", &x);
    int result = next_lucky_number(x);
    printf("%d\n", result);
    return 0;
}
