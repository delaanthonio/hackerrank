import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;
import java.util.HashSet;
import java.util.Queue;
import java.util.LinkedList;

/**
 * Roads and Libraries
 *
 * @author Dela Anthonio
 * @hackerrank https://hackerrank.com/delaanthonio
 * @problem https://www.hackerrank.com/challenges/torque-and-development
 */
public class solution {
	private static int buildRoads(List<List<Integer>> hackerLand, Set<Integer> seen, int start) {
		Queue<Integer> visiting = new LinkedList<>();
		visiting.add(start);
		seen.add(start);
		int newRoads = 0;

		while (!visiting.isEmpty()) {
			int city = visiting.remove();
			for (int neighbor : hackerLand.get(city)) {
				if (!seen.contains(neighbor)) {
					newRoads++;
					seen.add(neighbor);
					visiting.add(neighbor);
				}
			}
		}

		return newRoads;
	}

	private static long buildCost(List<List<Integer>> hackerLand, long libraryCost, long roadCost) {
		long cityGroups = 0;
		long roadsBuilt = 0;
		Set<Integer> seen = new HashSet<>();

		if (libraryCost <= roadCost) {
			return libraryCost * hackerLand.size();
		}

		for (int city = 0; city < hackerLand.size(); city++) {
			if (!seen.contains(city)) {
				cityGroups += 1;
				roadsBuilt += buildRoads(hackerLand, seen, city);
			}
		}

		return roadsBuilt * roadCost + cityGroups * libraryCost;
	}

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int q = scan.nextInt();
		List<List<Integer>> hackerLand = new ArrayList<List<Integer>>();
		for (int i = 0; i < q; i++) {
			int cityCount = scan.nextInt();
			int roadCount = scan.nextInt();
			int libraryCost = scan.nextInt();
			int roadCost = scan.nextInt();

			hackerLand.clear();

			for (int j = 0; j < cityCount; j++) {
				hackerLand.add(new ArrayList<Integer>());
			}

			for (int j = 0; j < roadCount; j++) {
				int src = scan.nextInt() - 1;
				int dst = scan.nextInt() - 1;
				hackerLand.get(src).add(dst);
				hackerLand.get(dst).add(src);
			}

			long cost = buildCost(hackerLand, libraryCost, roadCost);
			System.out.println(cost);
		}
		scan.close();
	}
}
