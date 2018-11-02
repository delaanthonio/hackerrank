import java.util.Scanner;

/**
 * Java Strings Introduction
 *
 * @author Dela Anthonio
 * @hackerrank https://hackerrank.com/delaanthonio
 * @problem https://www.hackerrank.com/challenges/java-strings-introduction
 */
public class solution {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String a = scan.next();
		String b = scan.next();
		StringBuilder sb = new StringBuilder();
		sb.append(Character.toUpperCase(a.charAt(0)));
		sb.append(a.substring(1));
		sb.append(" ");
		sb.append(Character.toUpperCase(b.charAt(0)));
		sb.append(b.substring(1));
		System.out.println(a.length() + b.length());
		System.out.println(a.compareTo(b) > 0 ? "Yes" : "No");
		System.out.println(sb);
		scan.close();
	}
}
