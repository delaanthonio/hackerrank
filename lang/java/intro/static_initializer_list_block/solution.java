import java.util.*;

/**
 * Java Static Initializer Block
 *
 * @author Dela Anthonio
 * @hackerrank https://hackerrank.com/delaanthonio
 * @problem https://www.hackerrank.com/challenges/java-static-initializer-block
 */
public class solution {
	static int B;
	static int H;
	static Boolean flag = true;

	static {
		Scanner scan = new Scanner(System.in);
		B = scan.nextInt();
		H = scan.nextInt();
		try {
			if (B < 1 || H < 1) {
				throw new Exception("Breadth and height must be positive");
			}
		}
		catch (Exception e) {
			System.out.println(e);
			flag = false;
		}
		scan.close();
	}

	public static void main(String[] args) {
		if (flag) {
			int area = B * H;
			System.out.println(area);
		}
	}
}
