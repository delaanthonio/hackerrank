import java.util.Scanner;
import java.util.regex.Pattern;
import java.util.regex.PatternSyntaxException;

/**
 * Pattern Syntax Checker
 *
 * @author Dela Anthonio
 * @hackerrank https://hackerrank.com/delaanthonio
 * @problem https://www.hackerrank.com/challenges/pattern-syntax-checker
 */
public class solution {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		while (scan.hasNext()) {
			String regex = scan.next();
			try {
				Pattern.compile(regex);
				System.out.println("Valid");
			}
			catch (PatternSyntaxException e) {
				System.out.println("Invalid");
			}
		}
		scan.close();
	}
}
