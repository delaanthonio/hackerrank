import java.util.InputMismatchException;
import java.util.Scanner;

/**
 * Java Datatypes
 *
 * @author Dela Anthonio
 * @hackerrank https://hackerrank.com/delaanthonio
 * @problem https://www.hackerrank.com/challenges/java-datatypes
 */
public class solution {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		long num = 0;
		for (int i = 0; i < n; i++) {
			try {
				num = scan.nextLong();
			}
			catch (InputMismatchException e) {
				System.out.printf("%s can't be fitted anywhere.\n", scan.next());
				continue;
			}
			System.out.printf("%s can be fitted in: \n", num);
			if (Byte.MIN_VALUE <= num && num <= Byte.MAX_VALUE) {
				System.out.println("* byte");
			}
			if (Short.MIN_VALUE <= num && num <= Short.MAX_VALUE) {
				System.out.println("* short");
			}
			if (Integer.MIN_VALUE <= num && num <= Integer.MAX_VALUE) {
				System.out.println("* int");
			}
			System.out.println("* long");
		}
	}
}
