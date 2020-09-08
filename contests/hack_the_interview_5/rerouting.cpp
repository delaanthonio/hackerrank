#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'getMinConnectionChange' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY connection as parameter.
 */

const int MAX_SIZE = 300000;

/**
 * A simple Union Find
 */
class UnionFind {
  public:
    vector<int> parents;
    vector<int> sizes;

    UnionFind(const int size) {
        for (int i = 0; i < size; i++) {
            parents.push_back(i);
            sizes.push_back(1);
        }
    }

    int find(const int x);
    bool merge(const int x, const int y);
};

int UnionFind::find(int x) {
    int parent = x;
    while (parents[parent] != parent) {
        parent = parents[parent];
    }
    parents[x] = parent;
    return parent;
}

bool UnionFind::merge(int x, int y) {
    int px = find(x);
    int py = find(y);
    if (px == py) {
        return false;
    }
    parents[px] = py;
    sizes[py] += sizes[px];
    return true;
}

int get_min_connection_change(vector<int> &connection) {
    int changes = connection.size();
    UnionFind uf(connection.size());
    for (int i = 0; i < connection.size(); i++) {
        if (uf.merge(i, connection[i] - 1)) {
            changes--;
        }
    }

    // Check if there is a terminal node.
    for (int i = 0; i < connection.size(); i++) {
        int root = uf.find(i);
        if (connection[root] == root + 1) {
            return changes - 1;
        }
    }

    // No terminal node. Create one using an extra change.
    return changes;
}

int main() {
    ofstream fout(getenv("OUTPUT_PATH"));

    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    string connection_temp_temp;
    getline(cin, connection_temp_temp);

    vector<string> connection_temp = split(rtrim(connection_temp_temp));

    vector<int> connection(n);

    for (int i = 0; i < n; i++) {
        int connection_item = stoi(connection_temp[i]);

        connection[i] = connection_item;
    }

    int result = get_min_connection_change(connection);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(s.begin(),
            find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace))));

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end());

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
