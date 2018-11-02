import java.util.Scanner;

/**
 * Java Substring
 *
 * @author Dela Anthonio
 * @hackerrank https://hackerrank.com/delaanthonio
 * @problem https://www.hackerrank.com/challenges/java-substring
 */
public class solution {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String s = scan.next();
		int start = scan.nextInt();
		int end = scan.nextInt();

		System.out.println(s.substring(start, end));
		scan.close();
	}
}
