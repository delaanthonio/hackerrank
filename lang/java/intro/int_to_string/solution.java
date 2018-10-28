import java.util.*;

/**
 * Java Int to String
 *
 * @author Dela Anthonio
 * @hackerrank https://hackerrank.com/delaanthonio
 * @problem https://www.hackerrank.com/challenges/java-int-to-string
 */
public class solution {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		String s = Integer.toString(n);
		System.out.println(Integer.parseInt(s));
		scan.close();
	}
}
