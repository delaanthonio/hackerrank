#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'receivedText' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING S as parameter.
 */

string receivedText(string raw) {
    // WRITE DOWN YOUR CODE HERE
    vector<string> vec = {""};
    string *out = &vec[0];
    bool numLock = true;
    for (char const &c: raw) {
        if (c == '<') {
            vec.push_back("");
            out = &vec.back();
        } else if (c == '>') {
            out = &vec.begin();
        } else if (c == '*') {
            out->erase(out->length());
        } else if (c == '#') {
            numLock = !numLock;
        } else if (!numLock && isdigit(c)) {
            continue;
        } else {
            out->push_back(c); 
        }
    }
    return vec[0];
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string S;
    getline(cin, S);

    string result = receivedText(S);

    fout << result << "\n";

    fout.close();

    return 0;
}
