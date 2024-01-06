#include <iostream>
#include <vector>

using namespace std;

int main() {
    int K;
    cin >> K;

    vector<pair<int,int>> edges;

    int curr = 1;
    int value = 0;
    while (K > 0) {

        if (K-curr < 0) {
            edges.push_back({value+1, value+curr});
            value = value+curr;
            curr = 1;
            edges.push_back({1, value+1});
        } else {
            K -= curr;
            curr += 1;
            edges.push_back({value+curr-1, value+curr});
        }

    }
    edges.push_back({value+1, value+curr});
    value = value+curr;

    cout << value << " " << edges.size() << endl;
    for (int i = 0; i < edges.size(); i++) {
        cout << edges[i].first << " " << edges[i].second << endl;
    }

    return 0;

}
