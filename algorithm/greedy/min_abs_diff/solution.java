import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.Collections;


public class solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
		List<Integer> items = new ArrayList<>();

		int n = scanner.nextInt();

		while (scanner.hasNext()) {
			items.add(scanner.nextInt());
		}

		Collections.sort(items);
		List<Integer> differences = new ArrayList<>();

		for (int i = 0; i < items.size() - 1; i++) {
			differences.add(Math.abs(items.get(i) - items.get(i + 1)));
		}

		System.out.println(Collections.min(differences));
    }
}
