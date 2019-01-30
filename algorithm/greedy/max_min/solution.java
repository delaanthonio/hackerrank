import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;
import java.util.stream.IntStream;
import java.util.stream.LongStream;

/**
 * Max Min
 *
 * @author Dela Anthonio
 * @hackerrank https://hackerrank.com/delaanthonio
 * @problem https://www.hackerrank.com/challenges/angry-children
 */
public class solution {

	static long maxMin(int k, ArrayList<Long> arr) {
		Collections.sort(arr);
		IntStream indices = IntStream.rangeClosed(0, arr.size() - k);
		return indices
				.mapToLong(i -> arr.get(i + k - 1) - arr.get(i))
				.min()
				.getAsLong();
	}

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int n = scanner.nextInt();
		int k = scanner.nextInt();
		ArrayList<Long> arr = new ArrayList<>();
		while (scanner.hasNextLong()) {
			arr.add(scanner.nextLong());
		}
		System.out.println(maxMin(k, arr));
		scanner.close();
	}
}
