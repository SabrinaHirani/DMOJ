// TODO solve without performing bfs for every query

#include <iostream>
#include <vector>
#include <queue>
#include <map>
using namespace std;

int main() {

    long N, W, D;
    cin >> N >> W >> D;

    map<int, vector<int>> graph;
    for (int i = 0; i < W; i++) {
        int A, B;
        cin >> A >> B;
        graph[A].push_back(B);
    }

    vector<int> route(N+1);
    for (int i = 1; i <= N; i++) {
        cin >> route[i];
    }

    for (int i = 0; i < D; i++) {
        int X, Y;
        cin >> X >> Y;

        swap(route[X], route[Y]);

        queue<int> q;
        vector<int> dist(N + 1, -1);
        dist[1] = 0;

        int max = 1;
        while (route[max] != N) {
            q.push(route[max]);
            dist[route[max]] = max-1;
            max++;
        }
        q.push(route[max]);
        dist[route[max]] = max-1;
        max--;

        while (!q.empty()) {
            int next = q.front();
            q.pop();
            for (long k = 0; k < graph[next].size(); k++) {
                int t = graph[next][k];
                if (dist[t] == -1 || dist[next] + 1 < dist[t]) {
                    dist[t] = dist[next] + 1;
                    if (t == N) {
                        if (dist[t] < max) {
                            max = dist[t];
                        }
                    } else {
                        q.push(t);
                    }
                }
            }
        }

        cout << max << endl;

    }

    return 0;
}