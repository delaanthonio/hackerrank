import java.util.Scanner;
import java.util.HashMap;
import java.util.Map;

/**
 * Hash Tables: Ransom Note
 *
 * @author Dela Anthonio
 * @hackerrank https://hackerrank.com/delaanthonio
 * @problem https://www.hackerrank.com/challenges/ctci-ransom-note/problem
 */
public class solution {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int m = scan.nextInt();
		int n = scan.nextInt();
		Map<String, Integer> magazine = new HashMap<>();
		Map<String, Integer> note = new HashMap<>();

		for (int i = 0; i < m; i++) {
			String word = scan.next();
			magazine.put(word, magazine.getOrDefault(word, 0) + 1);
		}

		for (int i = 0; i < n; i++) {
			String word = scan.next();
			note.put(word, note.getOrDefault(word, 0) + 1);
			if (note.get(word) > magazine.getOrDefault(word, 0)) {
				System.out.println("No");
				return;
			}
		}

		System.out.println("Yes");
		scan.close();
	}
}
