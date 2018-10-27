import java.util.*;

/**
 * Java Stdin and Stdout I
 *
 * @author Dela Anthonio
 * @hackerrank https://hackerrank.com/delaanthonio
 * @problem https://www.hackerrank.com/challenges/java-stdin-and-stdout-1
 */
public class solution {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		while(scanner.hasNextInt()) {
			int a = scanner.nextInt();
			System.out.println(a);
		}
	}
}
