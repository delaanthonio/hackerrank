import java.util.*;

/**
 * Java If-Else
 *
 * @author Dela Anthonio
 * @hackerrank https://hackerrank.com/delaanthonio
 * @problem https://www.hackerrank.com/challenges/java-if-else
 */
public class solution {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int n = scanner.nextInt();
		if (n % 2 == 0 && (n <= 5 || n > 20)) {
			System.out.print("Not ");
		}
		System.out.println("Weird ");
	}
}
