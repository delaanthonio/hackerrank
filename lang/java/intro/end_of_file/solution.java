import java.util.Scanner;

/**
 * Java End-of-file
 *
 * @author Dela Anthonio
 * @hackerrank https://hackerrank.com/delaanthonio
 * @problem https://www.hackerrank.com/challenges/java-end-of-file
 */
public class solution {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		for (int i = 1; scan.hasNext(); i++) {
			System.out.printf("%d %s %n", i, scan.nextLine());
		}
		scan.close();
	}
}
