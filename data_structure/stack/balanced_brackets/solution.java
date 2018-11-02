import java.util.Scanner;
import java.util.HashSet;
import java.util.Set;
import java.util.Stack;
import java.util.Map;
import java.util.HashMap;

/**
 * Balanced Brackets
 *
 * @author Dela Anthonio
 * @hackerrank https://hackerrank.com/delaanthonio
 * @problem https://www.hackerrank.com/challenges/balanced-brackets
 */
public class solution {
	private static final Set<Character> openning;
	private static final Map<Character, Character> closing;

	static {
		openning = new HashSet<>();
		openning.add('{');
		openning.add('[');
		openning.add('(');

		closing = new HashMap<>();
		closing.put('}', '{');
		closing.put(']', '[');
		closing.put(')', '(');
	}

	private static Boolean isBalanced(String brackets) {
		Stack<Character> unmatched = new Stack<>();
		for (char b : brackets.toCharArray()) {
			if (openning.contains(b)) {
				unmatched.push(b);
			}
			else if (unmatched.isEmpty() || closing.get(b) != unmatched.pop()) {
				return false;
			}
		}
		return unmatched.isEmpty();
	}

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		for (int i = 0; i < n; i++) {
			String brackets = scan.next();
			if (isBalanced(brackets)) {
				System.out.println("YES");
			}
			else {
				System.out.println("NO");
			}
		}
		scan.close();
	}
}
