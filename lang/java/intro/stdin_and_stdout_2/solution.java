import java.util.*;

/**
 * Java Stdin and Stdout II
 *
 * @author Dela Anthonio
 * @hackerrank https://hackerrank.com/delaanthonio
 * @problem https://www.hackerrank.com/challenges/java-stdin-and-stdout
 */
public class solution {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int i = scanner.nextInt();
		double d = scanner.nextDouble();
		scanner.nextLine(); // End current line
		String s = scanner.nextLine();
		System.out.printf("String: %s\n", s);
		System.out.printf("Double: %s\n", d);
		System.out.printf("Int: %d\n", i);
	}
}
