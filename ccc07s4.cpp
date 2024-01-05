#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main() {
    int n;
    cin >> n;

    map<int,vector<int>> graph;

    int x, y;
    cin >> x >> y;
    while (!(x == 0 && y == 0)) {
        if (graph.find(y) == graph.end()) {
            vector<int> temp;
            graph[y] = temp;
        }
        graph[y].push_back(x);
        cin >> x >> y;
    }

    vector<int> paths(n+1, 0);
    paths[1] = 1;
    for (int i = 2; i <= n; i++) {
        if (graph.find(i) != graph.end()) {
            for (int j = 0; j < graph[i].size(); j++) {
                paths[i] += paths[graph[i][j]];
            }
        }
    }

    cout << paths[n] << endl;

    return 0;

}