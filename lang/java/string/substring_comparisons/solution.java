import java.util.Scanner;

/**
 * Java Substring Comparisons
 *
 * @author Dela Anthonio
 * @hackerrank https://hackerrank.com/delaanthonio
 * @problem https://www.hackerrank.com/challenges/java-string-compare
 */
public class solution {
	public static String getSmallestAndLargest(String s, int k) {
		String smallest = s.substring(0, k);
		String largest = s.substring(0, k);

		for (int i = k; i <= s.length(); i++) {
			String substring = s.substring(i - k, i);
			if (substring.compareTo(smallest) < 0) {
				smallest = substring;
			}
			else if (substring.compareTo(largest) > 0) {
				largest = substring;
			}
		}

		return smallest + "\n" + largest;
	}

	public static void main(String[] args) {

		Scanner scan = new Scanner(System.in);
		String s = scan.next();
		int k = scan.nextInt();

		System.out.println(getSmallestAndLargest(s, k));
		scan.close();
	}
}
