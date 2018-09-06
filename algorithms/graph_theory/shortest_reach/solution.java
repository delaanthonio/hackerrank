/**
 * Breadth First Search: Shortest Reach
 *
 * @author Dela Anthonio
 * @hackerrank https://hackerrank.com/delaanthonio
 * @problem  https://hackerrank.com/challenges/bfsshortreachd
 */

import java.util.*;

public class solution {

    static final int EDGE_LENGTH = 6;

    /**
     * Return the shortest distance from each node in graph to a start node.
     *
     * @time  O(v) where v is the amount of vertices in graph.
     * @space O(v)
     */
    static List<Integer> bfs(int[][] graph, int start) {
        List<Integer> distances = new ArrayList<Integer>();
        for (int i = 0; i < graph.length; i++) {
            distances.add(-1);
        }
        distances.set(start, 0);
        Queue<Integer> nodes = new LinkedList<Integer>();
        nodes.add(start);
        while (!nodes.isEmpty()) {
            Integer node = nodes.remove();
            int[] adjacent = graph[node];
            for (int adj = 0; adj < adjacent.length; adj++) {
                if (adjacent[adj] >= 1 && distances.get(adj) == -1) {
                    int distance = distances.get(node) + EDGE_LENGTH;
                    distances.set(adj, distance);
                    nodes.add(adj);
                }
            }
        }
        distances.remove(start);
        return distances;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        for (int i = 0; i < n; i++) {
            int nodes = scanner.nextInt();
            int edges = scanner.nextInt();
            int[][] graph = new int[nodes][nodes];
            for (int j = 0; j < edges; j++) {
                int n1 = scanner.nextInt() - 1;
                int n2 = scanner.nextInt() - 1;
                graph[n1][n2] = 1;
                graph[n2][n1] = 1;
            }
            int start = scanner.nextInt() - 1;
            List<Integer> distances = bfs(graph, start);
            for (int d : distances) {
                System.out.print(d + " ");
            }
            System.out.println();
        }
    }
}
