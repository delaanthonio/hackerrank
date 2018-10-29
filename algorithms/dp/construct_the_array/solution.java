import java.util.Scanner;

/**
 * Construct the Array
 *
 * @author Dela Anthonio
 * @hackerrank https://hackerrank.com/delaanthonio
 * @problem https://www.hackerrank.com/challenges/construct-the-array
 */
public class solution {
	private static long LIMIT = 1000000007;

	private static long countWays(int n, int k, int x) {
		long[] waysEndK = new long[n - 1];
		waysEndK[0] = 1;
		long[] waysEnd1 = new long[n - 1];

		for (int i = 1; i < n - 1; i++) {
			waysEndK[i] = (waysEndK[i - 1] * (k - 2) + waysEnd1[i - 1]) % LIMIT;
			waysEnd1[i] = (waysEndK[i - 1] * (k - 1)) % LIMIT;
		}

		if (x == 1) {
			return waysEnd1[waysEnd1.length - 1];
		}
		return waysEndK[waysEndK.length - 1];
	}

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		int k = scan.nextInt();
		int x = scan.nextInt();

		System.out.println(countWays(n, k, x));
		scan.close();
	}
}
