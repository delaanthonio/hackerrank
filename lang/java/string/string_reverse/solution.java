import java.util.Scanner;

/**
 * Java String Reverse
 *
 * @author Dela Anthonio
 * @hackerrank https://hackerrank.com/delaanthonio
 * @problem https://www.hackerrank.com/challenges/java-string-reverse
 */
public class solution {
	public static Boolean isPalindrome(String s) {
		return s.equals(new StringBuilder(s).reverse().toString());
	}

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String s = scan.next();

		if (isPalindrome(s)) {
			System.out.println("Yes");
		}
		else {
			System.out.println("No");
		}
		scan.close();
	}
}
