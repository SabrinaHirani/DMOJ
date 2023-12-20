#include <iostream>
#include <vector>
#include <map>
#include <queue>
#include <set>

using namespace std;

int main() {
    int N, W, D;
    cin >> N >> W >> D;

    map<int, vector<int>> graph;
    for (int i = 0; i < W; i++) {
        int A, B;
        cin >> A >> B;
        graph[B].push_back(A);
    }

    vector<int> dist(N+1, 1e9);
    dist[N] = 0;

    queue<int> q;
    q.push(N);
    while (!q.empty()) {
        int next = q.front();
        q.pop();
        for (int k = 0; k < graph[next].size(); k++) {
            int u = graph[next][k];
            if (dist[u] == 1e9 || dist[next] + 1 < dist[u]) {
                dist[u] = dist[next] + 1;
                q.push(u);
            }
        }
    }

    vector<int> route(N+1);
    for (int i = 1; i <= N; i++) {
        cin >> route[i];
    }

    set<pair<int, int>> sorting;
    for (int i = 0; i <= N; i++) {
        sorting.insert(make_pair(dist[route[i]]+i, i));
    }

    for (int i = 0; i < D; i++) {
        int X, Y;
        cin >> X >> Y;

        sorting.erase(make_pair(dist[route[X]]+X, X));
        sorting.erase(make_pair(dist[route[Y]]+Y, Y));

        swap(route[X], route[Y]);

        sorting.insert(make_pair(dist[route[X]]+X, X));
        sorting.insert(make_pair(dist[route[Y]]+Y, Y));

        cout << sorting.begin()->first-1 << endl;

    }

    return 0;
}