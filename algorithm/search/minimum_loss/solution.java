import java.util.NavigableMap;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeMap;
import java.util.stream.Stream;

/**
 * Minimum Loss
 *
 * @author Dela Anthonio
 * @hackerrank https://hackerrank.com/delaanthonio
 * @problem https://www.hackerrank.com/challenges/
 */
public class solution {

	static long minimumLoss(NavigableMap<Long, Long> priceMap) {
		Set<Long> prices = priceMap.keySet();
		long minimumLoss = prices
				.stream()
				.map(price -> {
					Long lowerPrice = priceMap.lowerKey(price);
					while (lowerPrice != null) {
						if (priceMap.get(price) < priceMap.get(lowerPrice)) {
							return price - lowerPrice;
						}
						lowerPrice = priceMap.lowerKey(lowerPrice);
					}
					return Long.MAX_VALUE;
				})
				.reduce(Math::min)
				.orElse(Long.MAX_VALUE);
		return minimumLoss;
	}

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		long dayLimit = scanner.nextInt();

		NavigableMap<Long, Long> priceMap = new TreeMap<>();
		long i = 0;

		while (scanner.hasNextLong()) {
			priceMap.put(scanner.nextLong(), i++);
		}

		System.out.println(minimumLoss(priceMap));
		scanner.close();
	}
}
