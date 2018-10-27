import java.util.Scanner;

/**
 * Java Output Formatting
 *
 * @author Dela Anthonio
 * @hackerrank https://hackerrank.com/delaanthonio
 * @problem https://www.hackerrank.com/challenges/java-output-formatting
 */
public class solution {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		System.out.println("================================");
		while (scan.hasNext()) {
			String s = scan.next();
			int n = scan.nextInt();
			System.out.printf("%-15s", s);
			System.out.printf("%03d%n", n);
		}
		System.out.println("================================");
		scan.close();
	}
}
