import java.util.Scanner;

/**
 * Java Loops II
 *
 * @author Dela Anthonio
 * @hackerrank https://hackerrank.com/delaanthonio
 * @problem https://www.hackerrank.com/challenges/java-loops
 */
public class solution {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int t = scan.nextInt();
		for (int i = 0; i < t; i++) {
			int a = scan.nextInt();
			int b = scan.nextInt();
			int n = scan.nextInt();
			for (int j = 0; j < n; j++) {
				a += (int) Math.pow(2, j) * b;
				System.out.printf("%d ", a);
			}
			System.out.println();
		}
		scan.close();

	}
}
