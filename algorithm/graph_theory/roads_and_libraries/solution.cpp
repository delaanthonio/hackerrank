// Roads and Libraries
//
// author: Dela Anthonio
// hackerrank: https://hackerrank.com/delaanthonio
// problem: https://www.hackerrank.com/challenges/torque-and-development

#include <algorithm>
#include <cmath>
#include <iostream>
#include <iterator>
#include <numeric>
#include <queue>
#include <sstream>
#include <unordered_set>
#include <vector>

using namespace std;

long build_roads(vector<vector<int>> &hacker_land, unordered_set<int> &seen,
                 int start) {
    long new_roads = 0;
    queue<int> visiting({start});
    seen.insert(start);

    while (!visiting.empty()) {
        int city = visiting.front();
        visiting.pop();
        vector<int> &adjacent = hacker_land[city];
        for (auto it = adjacent.begin(); it != adjacent.end(); it++) {
            if (!seen.count(*it)) {
                new_roads++;
                seen.insert(*it);
                visiting.push(*it);
            }
        }
    }

    return new_roads;
}

long build_cost(vector<vector<int>> &hacker_land, int library_cost,
                int road_cost) {
    long cost = 0;
    unordered_set<int> seen;

    if (library_cost <= road_cost) {
        return library_cost * hacker_land.size();
    }

    for (size_t city = 0; city < hacker_land.size(); city++) {
        if (!seen.count(city)) {
            cost += library_cost;
            cost += road_cost * build_roads(hacker_land, seen, city);
        }
    }

    return cost;
}

int main() {
    ios_base::sync_with_stdio(false);
    int q;

    cin >> q;
    for (int i = 0; i < q; i++) {
        int cities;
        int roads;
        int library_cost;
        int road_cost;
        cin >> cities >> roads >> library_cost >> road_cost;
        vector<vector<int>> hacker_land(cities);

        for (int j = 0; j < roads; j++) {
            int src;
            int dst;
            cin >> src >> dst;
            src--;
            dst--;
            hacker_land[src].push_back(dst);
            hacker_land[dst].push_back(src);
        }

        long cost = build_cost(hacker_land, library_cost, road_cost);
        cout << cost << endl;
    }
    return 0;
}
